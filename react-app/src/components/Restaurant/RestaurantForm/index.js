import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import {
  thunkCreateRestaurant,
  thunkGetRestaurantDetail,
  thunkUpdateRestaurant,
} from "../../../store/restaurants";
import "./RestaurantForm.css"

export default function RestaurantForm({ formType, restaurantId }) {
  const dispatch = useDispatch();
  const history = useHistory();
  // const [menuItemImageFiles, setMenuItemImageFiles] = useState([]);
  // const [previewImageFile, setPreviewImageFile] = useState(null);
  const [streetAddress, setStreetAddress] = useState("");
  const [city, setCity] = useState("Gotham");
  const [state, setState] = useState("New York");
  const [postalCode, setPostalCode] = useState("");
  const [country, setCountry] = useState("United States");
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [hours, setHours] = useState("");
  const [previewImg, setPreviewImg] = useState("");

  const [validationObj, setValidationObj] = useState({});
  const [initialRestaurant, setInitialRestaurant] = useState({});

  const sessionUser = useSelector((stateid) => stateid.session.user);


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

    return errors;
  };

  const handleImages = () => {
    const imageUrls = [previewImg];
    const imageExtensionsRegex = /\.(png|jpe?g)$/i;
    const invalidImages = imageUrls.filter(
      (url) => url && !imageExtensionsRegex.test(url)
    );

    if (invalidImages.length > 0) {
      const errorsObj = { ...validationObj };
      invalidImages.forEach((url, index) => {
        const fieldName = index === 0 ? "previewImage" : `imageUrl${index + 1}`;
        errorsObj[fieldName] = "Image URL must end in .png, .jpg, or .jpeg";
      });
      setValidationObj(errorsObj);
      return false;
    }

    let newRestaurantImage = [];
    const tempNewRestaurantImage = [
      { url: previewImg, preview: true },
    ];

    tempNewRestaurantImage.forEach((image) => image.url && newRestaurantImage.push(image));
    return newRestaurantImage;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    let errorsObj = validateCommonFields();
    if (formType === "Create" && !previewImg)
      errorsObj.previewImg = "Preview Image is required";

    if (Object.keys(errorsObj).length) {
      setValidationObj(errorsObj);
      return;
    }
    const newRestaurantImage = handleImages();
    if (!newRestaurantImage) return;

    const restaurant = { name, streetAddress, city, state, postalCode, country, description, hours };
    try {

      if (formType === "Create") {
        const newlyCreateRestaurant = await dispatch(thunkCreateRestaurant(restaurant, newRestaurantImage, sessionUser));
        const newRestaurant = await dispatch(thunkGetRestaurantDetail(newlyCreateRestaurant.id));
        if (newRestaurant) history.push(`/restaurants/${newRestaurant.id}`);
        else throw new Error("Failed to create a new restaurant");
      }
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
      <select
        type="text"
        name="city"
        value={city}
        onChange={handleInputChange(setCity, "city")}
        className="select-form"
        required
      >
        <option value="Gotham">Gotham</option>
      </select>

      <select
        type="text"
        name="state"
        value={state}
        onChange={handleInputChange(setState, "state")}
        className="select-form"
        required
      >
        <option value="New York">New York</option>
      </select>
      <input
        type="text"
        name="postalCode"
        value={postalCode}
        onChange={handleInputChange(setPostalCode, "postalCode")}
        placeholder="Postal Code"
        className="input-form-postal"
        required
      />
      {validationObj.postalCode && (<p className="errors">{validationObj.postalCode}</p>)}
      <select
        type="text"
        name="country"
        value={country}
        onChange={handleInputChange(setCountry, "country")}
        className="select-form"
        required
      >
        <option value="United States">United States</option>
      </select>
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
          {validationObj.previewImg && (<p className="errors">{validationObj.previewImg}</p>)}
        </>
      )}

      {/* <input type="file" name="menu_item_images" onChange={setMenuItemImageFiles([...e.target.files])} multiple required /> */}
      {/* <input type="file" name="preview_image" onChange={setPreviewImageFile(e.target.files[0])} required /> */}
      <button type="submit" className="bttn-submit" disabled={Object.keys(validationObj).length > 0}>{formType === "Create" ? "Create Restaurant" : "Update Restaurant"}</button>
    </form>
  );
}
