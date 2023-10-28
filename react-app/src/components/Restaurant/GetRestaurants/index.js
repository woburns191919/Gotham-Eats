import React, { useEffect, useState } from "react";
import { Link, useHistory, NavLink, useParams } from "react-router-dom";
import "./GetRestaurants.css";
import DeleteRestaurant from "../DeleteRestaurant";
import OpenModalButton from "../../OpenModalButton";

export default function GetRestaurants({ ownerMode = false }) {
  const history = useHistory();
  const { id } = useParams();
  const [allRestaurants, setAllRestaurants] = useState();
  const [currentUser, setCurrentUser] = useState(null);
  const [filteredRestaurants, setFilteredRestaurants] = useState(null);
  
  const fetchCurrentUser = async () => {
    try {
      const res = await fetch("/api/auth/current_user");
      if (res.ok) {
        const data = await res.json();
        return data;
      } else {
        console.error("Failed to fetch user. Status:", res.status);
        return [];
      }
    } catch (error) {
      console.error("Failed to fetch user:", error);
      return [];
    }
  };

  const fetchAllRestaurants = async () => {
    try {
      const res = await fetch("/api/restaurants");
      if (res.ok) {
        const data = await res.json();
        return data.restaurants;
      } else {
        console.error("Failed to fetch restaurants. Status:", res.status);
        return [];
      }
    } catch (error) {
      console.error("Failed to fetch restaurants:", error);
      return [];
    }
  };


  useEffect(() => {
    // Fetch all restaurants
    (async function () {
      const allRestaurantData = await fetchAllRestaurants();
      setAllRestaurants(allRestaurantData);
    })();
  }, []);

  useEffect(() => {
    // Fetch current user
    (async function () {
      const currentUserData = await fetchCurrentUser();
      setCurrentUser(currentUserData);
    })();
  }, []);

  useEffect(() => {
    const ownedRestaurants =
      allRestaurants &&
      allRestaurants?.filter(
        (restaurant) => restaurant?.owner_id === currentUser?.id
      );

    setFilteredRestaurants(ownedRestaurants);
  }, [currentUser, allRestaurants]);

  const handleDelete = async (restId) => {
    try {
      const response = await fetch(`/api/restaurants/delete/${restId}`, {
        method: "DELETE",
      });

      if (response.ok) {
        history.push(`/owner/restaurants/${currentUser.id}`);
      } else {
        console.error("Failed to delete restaurant. Status:", response.status);
        const errorData = await response.json();
        console.error("Error data:", errorData);
      }
    } catch (error) {
      console.error("Failed to delete restaurant: ", error);
    }
  };

  return (
    <div className="main-container">
      {ownerMode && (
        <div className="owner-div manage-create-a-new-restaurant">
          <h2 className="manage-restaurants-h1-tag">Manage Your Restaurants</h2>

          <button className="owner-btn create-new-restaurant-btn">
            <NavLink
              to="/restaurants/new"
              className="create-new-restaurant-owner"
              style={{ textDecoration: "none", color: "var(--white)" }}
            >
              Create a New Restaurant
            </NavLink>
          </button>
        </div>
      )}

      <div className="ownerRestaurant-main-container ownerRestaurant-grid-container">
        {ownerMode
          ? filteredRestaurants?.map((restaurant, i) => (
              <div
                key={restaurant.id}
                className="ownerRestaurant-restaurant-img-main-div"
              >
                <Link
                  to={`/restaurants/${restaurant.id}`}
                  style={{ textDecoration: "none", color: "var(--black)" }}
                >
                  <div className="ownerRestaurant">
                    <img
                      src={
                        restaurant.menu_item_images.find((img) => img.preview)
                          ?.url || restaurant.preview_image_url
                      }
                      className="ownerRestaurant-img"
                      alt=""
                    />
                    <div className="owner-div update-delete-btns">
                      <Link
                        to={`/restaurants/edit/${restaurant.id}`}
                        style={{ textDecoration: "none", color: "var(--black)" }}
                      >
                        <button className="owner-btn post-delete-review-btn">
                          Update
                        </button>
                      </Link>
                      <button
                        className="owner-btn post-delete-review-btn"
                        onClick={() => handleDelete(restaurant.id)}
                      >
                        Delete
                      </button>
                    </div>

                    <div key={i} className="restaurant-info-flex">
                      <p className="res-name">
                        {restaurant.name} ({restaurant.streetAddress})
                      </p>
                      <p className="avgRating-p-tag">
                        {restaurant.avgRating !== null &&
                        restaurant.avgRating !== undefined
                          ? restaurant.avgRating.toFixed(1)
                          : <span className="boldText">New</span>}
                      </p>
                    </div>
                  </div>
                </Link>
              </div>
            ))
          : allRestaurants?.map((restaurant, i) => (
              <div
                className={`${
                  ownerMode
                    ? "ownerRestaurant-restaurant-img-main-div"
                    : "restaurant-img-main-div"
                }`}
                key={restaurant.id}
              >
                <Link
                  to={`/restaurants/${restaurant.id}`}
                  style={{ textDecoration: "none", color: "var(--black)" }}
                >
                  <div
                    className={`restaurant-box ${
                      ownerMode ? "ownerRestaurant" : ""
                    }`}
                  >
                    <img
                      src={
                        restaurant.menu_item_images.find((img) => img.preview)
                          ?.url || restaurant.preview_image_url
                      }
                      className={
                        ownerMode ? "ownerRestaurant-img" : "restaurant-img"
                      }
                      alt=""
                    />

                    <div key={i} className="restaurant-info-flex">
                      <p className="res-name">
                        {restaurant.name} ({restaurant.streetAddress})
                      </p>
                      <p className="avgRating-p-tag">
                        {restaurant.avgRating !== null &&
                        restaurant.avgRating !== undefined
                          ? restaurant.avgRating.toFixed(1)
                          : <span className="boldText">New</span>}
                      </p>
                    </div>
                  </div>
                </Link>
              </div>
            ))}
      </div>
    </div>
  );
}
