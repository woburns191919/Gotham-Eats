import React, { useState } from "react";
import { useHistory } from "react-router-dom";

const DeleteRestaurant = ({ restaurantId }) => {
  const history = useHistory();
  const [isDeleting, setIsDeleting] = useState(false);

  const handleDelete = async () => {
    try {
      setIsDeleting(true);

      const response = await fetch(`/api/restaurants/delete/${restaurantId}`, {
        method: "DELETE",
      });

      if (response.ok) {
     
        setRestaurants((prevRestaurants) =>
          prevRestaurants.filter((restaurant) => restaurant.id !== restaurantId)
        );

        history.push("/restaurants");
      } else {
        console.error("Failed to delete restaurant.");
      }
    } catch (error) {
      console.error("Failed to delete restaurant: ", error);
    }
  };


  return (
    <div>
      <p>Are you sure you want to delete this restaurant?</p>
      <button onClick={handleDelete} disabled={isDeleting}>
        {isDeleting ? "Deleting..." : "Delete"}
      </button>
    </div>
  );
};

export default DeleteRestaurant;
