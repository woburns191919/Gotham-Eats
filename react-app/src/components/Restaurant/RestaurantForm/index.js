import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import "./RestaurantForm.css";

export default function RestaurantForm({ formType }) {
  const history = useHistory();
  const { restaurantId } = useParams();
  const [restaurant, setRestaurant] = useState();
  const [currentUser, setCurrentUser] = useState(null);
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
  const [previewImgUrl, setPreviewImgUrl] = useState("");

  const [validationObj, setValidationObj] = useState({});
  const [initialRestaurant, setInitialRestaurant] = useState({});

  const sessionUser = useSelector((state) => state.session.user);

  const fetchRestaurant = async () => {
    try {
      const res = await fetch(`/api/restaurants/${restaurantId}`);
      if (res.ok) {
        const data = await res.json();
        return data;
      } else {
        console.error('Failed to fetch restaurant data:', res.status);
        return null;
      }
    } catch (error) {
      console.error('Error in fetchRestaurant:', error);
      return null;
    }
  };

  useEffect(() => {
   
    const fetchData = async () => {
      try {
        if (formType === "Edit" && restaurantId) {
          const res = await fetchRestaurant();
          console.log('res from restaurant form use effect', res)
          if (res) {
            setName(res.name);
            setStreetAddress(res.streetAddress);
            setCity(res.city);
            setState(res.state);
            setPostalCode(res.postalCode);
            setCountry(res.country);
            setDescription(res.description);
            setHours(res.hours);
            setPreviewImgUrl(res.previmg);
            setInitialRestaurant(res);
          } else {
            console.error("Failed to fetch restaurant data.");
          }
        }
      } catch (error) {
        console.error("Error fetching restaurant data:", error);
      }
    };

    fetchData();
  }, [formType, restaurantId]);


  const fetchHandleRestaurant = async (restaurantId, restaurantData) => {

    if (formType === "Edit") {
      try {
        const res = await fetch(`/api/restaurants/edit/${restaurantId}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(restaurantData),
        });

        if (res.ok) {
          history.push(`/restaurants/edit/${restaurantId}`);
        } else {
          console.error("Failed to update restaurant.");
        }
      } catch (error) {
        console.error("Error updating restaurant:", error.message);
      }
    } else if (formType === "Create") {
      const res = await fetch(`/api/restaurants/new`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(restaurantData),
      });

      if (res.ok) {
        const data = await res.json();
        history.push("/restaurants");
        return data;
      } else {
        console.error("Failed to fetch");
        return [];
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
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
      preview_image_url: previewImgUrl,
    };
    try {
      fetchHandleRestaurant(restaurantId, restaurantData);
    } catch (error) {
      console.error("Error processing restaurant:", error.message);
    }
  };

  const clearValidationError = (validationField) => {
    setValidationObj((prev) => {
      const newObj = { ...prev };
      delete newObj[validationField];
      return newObj;
    });
  };

  const handleInputChange = (setterFunction, validationField) => (e) => {
    const value = e.target.value;
    console.log(`Setting ${validationField} to:`, value);
    setterFunction(value);
    clearValidationError(validationField);
  };

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
      />
      {validationObj.name && <p className="errors">{validationObj.name}</p>}
      <input
        type="text"
        name="streetAddress"
        value={streetAddress}
        onChange={handleInputChange(setStreetAddress, "streetAddress")}
        placeholder="Street Address"
        className="input-form"
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
      >
        <option value="Gotham">Gotham</option>
      </select>
      <select
        type="text"
        name="state"
        value={state}
        onChange={handleInputChange(setState, "state")}
        className="select-form"
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
      >
        <option value="United States">United States</option>
      </select>
      <textarea
        name="description"
        value={description}
        onChange={handleInputChange(setDescription, "description")}
        placeholder="Description"
        className="textarea-form"
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
      />
      {validationObj.hours && <p className="errors">{validationObj.hours}</p>}
      {formType === "Create" && (
        <>
          <input
            type="url"
            value={previewImgUrl}
            className="photo-input"
            placeholder="Show Off Your Dish With a Photo URL"
            onChange={(e) => setPreviewImgUrl(e.target.value)}
            required
          />
          {/* {validationObj.previewImg && (
              <p className="errors">{validationObj.previewImg}</p>
            )} */}
        </>
      )}
      <button
        type="submit"
        className="bttn-submit"
        // disabled={Object.keys(validationObj).length > 0}
      >
        {formType === "Create" ? "Create Restaurant" : "Update Restaurant"}
      </button>

    </form>
  );
}
