import React, { useEffect, useState } from "react";
import { Link, useHistory, NavLink } from "react-router-dom";
import "./GetRestaurants.css";


export default function AllRestaurantComponent({
  ownerMode = false,
  previewImgUrl,
}) {
  const history = useHistory();
  const [restaurants, setRestaurants] = useState();
  const [currentUser, setCurrentUser] = useState(null);
  const [filteredRestaurants, setFilteredRestaurants] = useState(null);

  const fetchRestaurants = async () => {
    const res = await fetch("/api/restaurants");
    if (res.ok) {
      const data = await res.json();
      return data.restaurants;
    } else {
      console.error("Failed to fetch");
      return [];
    }
  };
  const fetchCurrentUser = async () => {
    const res = await fetch("/api/auth/current_user");
    if (res.ok) {
      const data = await res.json();
      return data;
    } else {
      console.error("Failed to fetch user");
      return [];
    }
  };

  useEffect(() => {
    (async function () {
      const restaurantData = await fetchRestaurants();
      setRestaurants(restaurantData);
    })();
  }, []);

  useEffect(() => {
    (async function () {
      const currentUserData = await fetchCurrentUser();
      setCurrentUser(currentUserData);
    })();
  }, []);

  useEffect(() => {
    const ownedRestaurants = restaurants?.filter(
      (restaurant) => restaurant?.owner_id === currentUser?.id
    );
    // console.log('restaurant data from fetch', ownedRestaurants)
    setFilteredRestaurants(ownedRestaurants);
  }, [currentUser, restaurants]);

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
                {console.log("restaurant id", restaurant)}
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
                      <button
                        className="owner-btn post-delete-review-btn"
                        onClick={() =>
                          history.push(`/restaurants/edit/${restaurant.id}`)
                        }
                      >
                        Update
                      </button>
                      <button
                        className="owner-btn post-delete-review-btn"
                        onClick={() =>
                          history.push(`/restaurants/edit/${restaurant.id}`)
                        }
                      >
                        Delete
                      </button>
                      {/*LETS GET TH IS UP AND RUNNING BOYS <OpenModalButton buttonText="Delete" modalComponent={<DeleteRestaurant restaurantId={restaurant.id} />} /> */}
                    </div>

                    <div key={i} className="restaurant-info-flex">
                      <p className="res-name">
                        {restaurant.name}({restaurant.streetAddress})
                      </p>
                      <p className="avgRating-p-tag">
                        {/* {restaurant.avgRating && restaurant.avgRating ? restaurant.avgRating?.toFixed(1) : <span className="boldText">New</span>} */}
                        {restaurant.avgRating !== null &&
                        restaurant.avgRating !== undefined ? (
                          restaurant.avgRating.toFixed(1)
                        ) : (
                          <span className="boldText">New</span>
                        )}
                      </p>
                    </div>
                  </div>
                </Link>
              </div>
            ))
          : restaurants?.map((restaurant, i) => (
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
                        {restaurant.name}({restaurant.streetAddress})
                      </p>
                      <p className="avgRating-p-tag">
                        {/* {restaurant.avgRating && restaurant.avgRating ? restaurant.avgRating?.toFixed(1) : <span className="boldText">New</span>} */}
                        {restaurant.avgRating !== null &&
                        restaurant.avgRating !== undefined ? (
                          restaurant.avgRating.toFixed(1)
                        ) : (
                          <span className="boldText">New</span>
                        )}
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
