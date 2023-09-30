import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import {
  thunkCreateRestaurant,
  thunkGetRestaurantDetail,
  thunkUpdateRestaurant,
  actionSetCreatedRestaurant
} from "../../../store/restaurants";
import "./RestaurantForm.css"

export default function CreateRestaurantForm({ formType, restaurantId }) {
  const dispatch = useDispatch();
  const history = useHistory();
  // const [menuItemImageFiles, setMenuItemImageFiles] = useState([]);
  // const [previewImageFile, setPreviewImageFile] = useState(null);
  const [streetAddress, setStreetAddress] = formType==='Create'?useState(""): useState()
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [postalCode, setPostalCode] = useState("");
  const [country, setCountry] = useState("");
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [hours, setHours] = useState("");
  const [previewImg, setPreviewImg] = useState("");

  const [validationObj, setValidationObj] = useState({});
  const [initialRestaurant, setInitialRestaurant] = useState({});

  const sessionUser = useSelector((state) => state.session.user);
  const oneRestaurant = useSelector((state) => state.restaurants?.singleRestaurant);


  useEffect(() => {
    if (formType === "Edit" && restaurantId) {
      dispatch(thunkGetRestaurantDetail(restaurantId)).then((data) => {
        setName(data.name);
        setStreetAddress(data.streetAddress);
        setCity(data.city);
        setState(data.state);
        setPostalCode(data.postalCode);
        setCountry(data.country);
        setDescription(data.description);
        setHours(data.hours);

        setInitialRestaurant(data);
      });
    }
  }, [dispatch, formType, restaurantId]);

  const clearValidationError = (validationField) => {
    setValidationObj((prev) => {
      const newObj = { ...prev };
      delete newObj[validationField];
      return newObj;
    });
  };

  const handleInputChange = (setterFunction, validationField) => (e) => {
    setterFunction(e.target.value);
    clearValidationError(validationField);
  };

  const validateCommonFields = () => {
    const errors = {};
    if (!name) errors.name = "Name is required";
    if (!streetAddress) errors.streetAddress = "Street Address is required";
    if (description.length < 10) errors.description = "Description needs a minimum of 10 characters";
    if (!hours) errors.hours = "Hours is required";
    if (postalCode.length !== 5) errors.postalCode = "Zip must be 5 characters";
    // if (String(postalCode).length !== 5) errors.postalCode = "Zip must be 5 characters";

    return errors;
  };


  // const isImageUrlValid = (imageUrl) => /\.(jpg|jpeg|png)$/i.test(imageUrl);

  // const handleImage = (previewImg) => {
  //   if (isImageUrlValid(previewImg)) {
  //     console.log("Image URL is valid");
  //   } else {
  //     console.error("Image URL must end in .jpg, .jpeg, or .png");
  //   }
  // };
  const handleCreateRestaurant = async (restaurantData) => {
    const resultAction = await dispatch(thunkCreateRestaurant(restaurantData));
    if (thunkCreateRestaurant.fulfilled.match(resultAction)) {
      const newlyCreatedRestaurant = resultAction.payload;
      dispatch(actionSetCreatedRestaurant(newlyCreatedRestaurant));
      history.push(`/restaurants/${newlyCreatedRestaurant.id}`);
    }
  };


  const handleSubmit = async (e) => {
    e.preventDefault();
    let errorsObj = validateCommonFields();
    // if (formType === "Create" && !previewImg)
    //   errorsObj.previewImg = "Preview Image is required";

    if (Object.keys(errorsObj).length) {
      setValidationObj(errorsObj);
      return;
    }

    // const newRestaurantImage = handleImages();
    // if (!newRestaurantImage) return;

    // const restaurant = { name, streetAddress, city, state, postalCode, country, description, hours, newRestaurantImage };
    const restaurant = {owner_id: sessionUser.id, name, streetAddress, city, state, postalCode, country, description, hours, preview_image_url: previewImg, preview: true};
    console.log("******************owner_id: ", restaurant.owner_id)
    console.log("******************name: ", restaurant.name)
    console.log("******************streetAddress: ", restaurant.streetAddress)
    console.log("******************city: ", restaurant.city)
    console.log("******************state: ", restaurant.state)
    console.log("******************postalCode: ", restaurant.postalCode)
    console.log("******************country: ", restaurant.country)
    console.log("******************description: ", restaurant.description)
    console.log("******************hours: ", restaurant.hours)
    console.log("******************preview_image_url: ", restaurant.preview_image_url)
    console.log("******************preview: ", restaurant.preview)

    try {

      if (formType === "Create") handleCreateRestaurant (restaurant);

      if (formType === "Edit") {
        const updatedRestaurant = { ...initialRestaurant, name, streetAddress, city, state, postalCode, country, description, hours };
        const updatedRestaurantData = await dispatch(thunkUpdateRestaurant(updatedRestaurant));
        if (updatedRestaurantData) history.push(`/restaurants/${updatedRestaurantData.id}`);
        else throw new Error("Failed to update your restaurant");
      }
    } catch (error) {
      console.error("Error processing the restaurant:", error.message);
    }
  };


  return (
    <form onSubmit={handleSubmit} className="restaurant-form">
      <h1 className="form-header-h1">
        {formType === "Create" ? "Create a Restaurant" : "Update your Restaurant"}
      </h1>
      <input
        type="text"
        name="name"
        value={name}
        onChange={handleInputChange(setName, "name")}
        placeholder="Name"
        className="input-form"
        required
      />
      {validationObj.name && <p className="errors">{validationObj.name}</p>}
      <input
        type="text"
        name="streetAddress"
        value={streetAddress}
        onChange={handleInputChange(setStreetAddress, "streetAddress")}
        placeholder="Street Address"
        className="input-form"
        required
      />
      {validationObj.streetAddress && (<p className="errors">{validationObj.streetAddress}</p>)}
      <div className="city-state-div">
        <select
          name="city"
          value={city}
          onChange={handleInputChange(setCity, "city")}
          className="select-form"
          required
        >
          <option value="" disabled selected>
            Select a City
          </option>
          <option value="Gotham">Gotham</option>
        </select>
        {validationObj.city && <p className="errors">{validationObj.city}</p>}

        <select
          name="state"
          value={state}
          onChange={handleInputChange(setState, "state")}
          className="select-form"
          required
        >
          <option value="" disabled selected>
            Select a State
          </option>
          <option value="New York">New York</option>
        </select>
        {validationObj.state && <p className="errors">{validationObj.state}</p>}
      </div>

      <input
        type="text"
        name="postalCode"
        value={postalCode}
        onChange={handleInputChange(setPostalCode, "postalCode")}
        placeholder="Postal Code"
        className="input-form-postal"
        required
      />
      {/* {validationObj.postalCode && (<p className="errors">{validationObj.postalCode}</p>)} */}

      <select
        name="country"
        value={country}
        onChange={handleInputChange(setCountry, "country")}
        className="select-form"
        required
      >
        <option value="" disabled selected>
          Select a Country
        </option>
        <option value="United States">United States</option>
      </select>
      {validationObj.country && (<p className="errors">{validationObj.country}</p>)}

      <textarea
        name="description"
        value={description}
        onChange={handleInputChange(setDescription, "description")}
        placeholder="Description"
        className="textarea-form"
        required
      />
      {validationObj.description && (<p className="errors">{validationObj.description}</p>)}
      <textarea
        name="hours"
        value={hours}
        onChange={handleInputChange(setHours, "hours")}
        placeholder="Hours"
        className="textarea-form"
        required
      />
      {validationObj.hours && (<p className="errors">{validationObj.hours}</p>)}
      {formType === "Create" && (
        <>
          <input type="url" className="photo-input" placeholder="Show Off Your Dish With a Photo URL" onChange={handleInputChange(setPreviewImg, "previewImg")} required />
          {/* {validationObj.previewImg && (<p className="errors">{validationObj.previewImg}</p>)} */}
        </>
      )}

      {/* <input type="file" name="menu_item_images" onChange={setMenuItemImageFiles([...e.target.files])} multiple required /> */}
      {/* <input type="file" name="preview_image" onChange={setPreviewImageFile(e.target.files[0])} required /> */}
      <button type="submit" className="bttn-submit" disabled={Object.keys(validationObj).length > 0}>{formType === "Create" ? "Create Restaurant" : "Update Restaurant"}</button>
    </form>
  );
}
