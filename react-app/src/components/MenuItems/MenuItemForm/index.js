import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import useFormValidation from "../../Inputs/handlesHelperFunctions";
import { useParams, useHistory } from "react-router-dom";

export default function MenuItemForm({ formType, menuItemId }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [type, setType] = useState("");
  const { id } = useParams();
  const [restId, setRestId] = useState(id);
  const [menuItem, setMenuItem] = useState("");

  const [validationObj, setValidationObj] = useState({});
  const [initialRestaurant, setInitialRestaurant] = useState({});

  const sessionUser = useSelector((stateid) => stateid.session.user);

  const fetchHandleMenuItem = async (menuItemData) => {
    const res = await fetch(
      `/api/restaurants/${restId}/menu_items`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(menuItemData),

      }
    );
    // console.log("data from post to db", menuItemData);
    // console.log('rest id from form', restId)
    // console.log('res', res)

    if (res.ok) {
        console.log('inside res ok?')
      const data = await res.json();
    //   console.log("req to db****", data);
      history.push(`/restaurants/${restId}`)
      console.log('data from form****', data)
      return data;
    } else {
      console.error("Failed to create menu item");
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const menuItemData = {
      restaurantId: restId,
      name,
      description,
      price,
      type,
    };
    try {
      fetchHandleMenuItem(menuItemData);
      history.push(`/restaurants/${restId}`);
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
    setterFunction(value);
    clearValidationError(validationField);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={handleInputChange(setName, "name")}
        />
      </label>
      <label>
        Description:
        <textarea
          value={description}
          onChange={handleInputChange(setDescription, "description")}
        />
      </label>
      <label>
        Price:
        <input
          type="number"
          value={price}
          onChange={handleInputChange(setPrice, "price")}
        />
      </label>
      <label>
        Type:
        <select value={type} onChange={handleInputChange(setType, "type")}>
          <option value="" disabled selected>
            Select a Menu Item Type
          </option>
          <option value="entree">Entree</option>
          <option value="dessert">Dessert</option>
          <option value="drink">Drink</option>
          <option value="side">Side</option>
        </select>
      </label>
      <button type="submit">Create Menu Item</button>
    </form>
  );
}
