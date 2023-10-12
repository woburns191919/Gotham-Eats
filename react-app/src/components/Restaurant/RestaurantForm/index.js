import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./RestaurantForm.css";

export default function RestaurantForm({ formType, restaurantId }) {
  const history = useHistory();
  const [restaurant, setRestaurant] = useState();
  const [currentUser, setCurrentUser] = useState(null);
  const [restId, setRestId] = useState(restaurantId);
  const [filteredRestaurants, setFilteredRestaurants] = useState(null);


  const dispatch = useDispatch();

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


  const clearValidationError = (validationField) => {
    setValidationObj((prev) => {
      const newObj = { ...prev };
      delete newObj[validationField];
      return newObj;
    });
  };

  const handleInputChange = (setterFunction, validationField) => (e) => {
    const url = e.target.value;
    console.log('URL:', url);
    setterFunction(url);
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




  // useEffect(() => {
  //   (async function () {
  //     const restaurantData = await fetchRestaurants();
  //     setRestaurant(restaurantData);
  //   })();
  // }, []);


  const handleSubmit = async (e) => {
    e.preventDefault();
    let errorsObj = validateCommonFields();
    if (formType === "Create" && !previewImg)
      errorsObj.previewImg = "Preview Image is required";

    if (Object.keys(errorsObj).length) {
      setValidationObj(errorsObj);
      return;
    }




    const restaurantData = {
      owner_id: sessionUser.id,
      name,
      street_address: streetAddress,
      city,
      state,
      postal_code: postalCode,
      country,
      description,
      hours,
      preview_image_url: previewImg
    };

      const res = await fetch(`/api/restaurants/new`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(restaurantData),
      });
      console.log('data?', restaurantData)
      if (res.ok) {
        const data = await res.json();
        console.log('data from post', data)

        return data;
      } else {
        console.error("Failed to fetch");
        return [];
      }
  }


    return (
      <form onSubmit={handleSubmit} className="restaurant-form">
        <h1 className="form-header-h1">
          {formType === "Create"
            ? "Create a Restaurant"
            : "Update your Restaurant"}
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
        {validationObj.streetAddress && (
          <p className="errors">{validationObj.streetAddress}</p>
        )}
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
        {validationObj.postalCode && (
          <p className="errors">{validationObj.postalCode}</p>
        )}
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
        {validationObj.description && (
          <p className="errors">{validationObj.description}</p>
        )}
        <textarea
          name="hours"
          value={hours}
          onChange={handleInputChange(setHours, "hours")}
          placeholder="Hours"
          className="textarea-form"
          required
        />
        {validationObj.hours && <p className="errors">{validationObj.hours}</p>}
        {formType === "Create" && (
          <>
            <input
              type="url"
              className="photo-input"
              placeholder="Show Off Your Dish With a Photo URL"
              onChange={handleInputChange(setPreviewImg, "previewImg")}
              required
            />
            {validationObj.previewImg && (
              <p className="errors">{validationObj.previewImg}</p>
            )}
          </>
        )}
        <button
          type="submit"
          className="bttn-submit"
          disabled={Object.keys(validationObj).length > 0}
        >
          {formType === "Create" ? "Create Restaurant" : "Update Restaurant"}
        </button>
      </form>
    );
  };
