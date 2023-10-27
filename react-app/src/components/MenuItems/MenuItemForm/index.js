import React, { useState, useEffect } from "react";
import { useHistory, useParams } from "react-router-dom";


export default function MenuItemForm({ formType }) {
  const history = useHistory();
  const { id, menuItemId } = useParams();
  const [restId, setRestId] = useState(id);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [type, setType] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [menuItemImageId, setMenuItemImageId] = useState("");
  const [validationObj, setValidationObj] = useState({});


  const fetchMenuItem = async () => {
    try {
      const res = await fetch(`/api/restaurants/${id}/menu_items/${menuItemId}`);
      if (res.ok) {
        const data = await res.json();
        return data;
      } else {
        console.error('Failed to fetch menu item data:', res.status);
        return null;
      }
    } catch (error) {
      console.error('Error in fetchMenuItem:', error);
      return null;
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (formType === "Edit" && menuItemId) {
          const res = await fetchMenuItem();
          console.log('res from useEffect', res)
          if (res) {
            setName(res.name);
            setDescription(res.description);
            setPrice(res.price);
            setType(res.type);
            setImageUrl(res.setImageUrl);

          } else {
            console.error("Failed to fetch restaurant data.");
          }
        }
      } catch (error) {
        console.error("Error fetching restaurant data:", error);
      }
    };

    fetchData();
  }, [formType, menuItemId]);

  const fetchHandleItem = async (menuItemData) => {
    if (formType === "Create") {
      try {
        const res = await fetch(`/api/restaurants/${restId}/menu_items`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(menuItemData),
        });

        if (res.ok) {
          const data = await res.json();
          console.log("data handle submit****", data);
          history.push(`/restaurants/${restId}`);
        } else {
          console.error("Failed to create menu item");
        }
      } catch (error) {
        console.error("Error processing restaurant:", error.message);
      }
    } else if (formType === "Edit") {
      try {
        const res = await fetch(
          `/api/restaurants/${id}/menu_items/${menuItemId}/edit`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(menuItemData),
          }
        );

        if (res.ok) {
          history.push(`restaurants/${id}/menu_items/${menuItemId}`);
        } else {
          console.error("Failed to update menu item.");
        }
      } catch (error) {
        console.error("Error updating menu item:", error.message);
      }
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
      itm_img_url: imageUrl,
    };
    try {
      fetchHandleItem(menuItemData);
    } catch (error) {
      console.error("Error processing menu item:", error.message);
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
        <select value={type}
        onChange={handleInputChange(setType, "type")}
        >
          <option value="" disabled>
            Select a Menu Item Type
          </option>
          <option value="entree">Entree</option>
          <option value="dessert">Dessert</option>
          <option value="drink">Drink</option>
          <option value="side">Side</option>
        </select>
      </label>
      <label>
        Image URL:
        <input
          type="text"
          value={imageUrl}
          onChange={handleInputChange(setImageUrl, "imageUrl")}
        />
      </label>

      <button
      type="submit"
      >
        {formType === "Create" ? "Create Menu Item" : "Update Menu Item"}
      </button>
      <img src={imageUrl} />
    </form>
  );
}
