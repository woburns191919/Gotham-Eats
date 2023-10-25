import React, { useState } from "react";
import { useHistory, useParams } from "react-router-dom";

export default function MenuItemForm() {
  const history = useHistory();
  const { id } = useParams();
  const [restId, setRestId] = useState(id);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [type, setType] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [menuItemImageId, setMenuItemImageId] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const menuItemData = {
      restaurantId: restId,
      name,
      description,
      price,
      type,
      url: imageUrl,
    //   menu_item_img_id: menuItemImageId
    };

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
        console.log('data handle submit', data);
        history.push(`/restaurants/${restId}`);
      } else {
        console.error("Failed to create menu item");
      }
    } catch (error) {
      console.error("Error processing restaurant:", error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <label>
        Description:
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </label>
      <label>
        Price:
        <input
          type="number"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
      </label>
      <label>
        Type:
        <select value={type} onChange={(e) => setType(e.target.value)}>
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
          onChange={(e) => setImageUrl(e.target.value)}
        />
      </label>

      <label>
        Menu Item Image ID:
        <input
          type="number"
          value={menuItemImageId}
          onChange={(e) => setMenuItemImageId(e.target.value)}
        />
      </label>

      <button type="submit">Create Menu Item</button>
      <img src={imageUrl} />
    </form>
  );
}
