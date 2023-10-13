import React, { useEffect, useState } from "react";
import { Link, useHistory, NavLink, useParams } from "react-router-dom";
import "./GetRestaurants.css";
import DeleteRestaurant from "../DeleteRestaurant";
import OpenModalButton from "../../OpenModalButton";

export default function AllRestaurantComponent({
  ownerMode = false,
  previewImgUrl,
}) {
  const history = useHistory();
  const { id } = useParams();
  const [allRestaurants, setAllRestaurants] = useState();
  const [currentUser, setCurrentUser] = useState(null);
  const [filteredRestaurants, setFilteredRestaurants] = useState(null);
  const [restId, setRestId] = useState(id);
  const [singleRestaurant, setSingleRestaurant] = useState(id);
  const [isDeleting, setIsDeleting] = useState(false);

  const fetchAllRestaurants = async () => {
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

  const fetchSingleRestaurant = async () => {
    const res = await fetch(`/api/restaurants/${restId}`);
    if (res.ok) {
      const data = await res.json();

      return data;
    } else {
      console.error("Failed to fetch");
      return [];
    }
  };

  useEffect(() => { // all restaurants
    (async function () {
      const allRestaurantData = await fetchAllRestaurants();
      setAllRestaurants(allRestaurantData);
    })();
  }, []);

  useEffect(() => { // for current user
    (async function () {
      const currentUserData = await fetchCurrentUser();
      setCurrentUser(currentUserData);
    })();
  }, []);

  useEffect(() => { //single restaurant detail
    (async function () {
      const singleRestaurantData = await fetchSingleRestaurant();
      setSingleRestaurant(singleRestaurant);
    })();
  }, []);


  useEffect(() => {
    const ownedRestaurants = allRestaurants && allRestaurants?.filter( //manage restaurants
      (restaurant) => restaurant?.owner_id === currentUser?.id
    );
    // console.log('restaurant data from fetch', ownedRestaurants)
    setFilteredRestaurants(ownedRestaurants);
  }, [currentUser, allRestaurants]);


  const handleDelete = async () => {
    try {
      setIsDeleting(true);

      const response = await fetch(`/api/restaurants/delete/${restId}`, {
        method: "DELETE",
      });

      if (response.ok) {

        setAllRestaurants((prevRestaurants) =>
          prevRestaurants.filter((restaurant) => restaurant.id !== restId)
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
                        onClick={handleDelete}

                      >
                        Delete
                      </button>

                      {/* <OpenModalButton buttonText="Delete" modalComponent={<DeleteRestaurant restaurantId={restaurant.id} /> } */}
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
