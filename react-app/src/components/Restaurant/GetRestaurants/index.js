import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useHistory, NavLink } from "react-router-dom";
import { thunkGetAllRestaurants } from "../../../store/restaurants";
import OpenModalButton from "../../OpenModalButton/index";
import "./GetRestaurants.css";

export default function GetRestaurants({ ownerMode = false }) {
  const dispatch = useDispatch();
  const history = useHistory();
  // const restaurants = useSelector((state) => state.restaurants.allRestaurants);
  const restaurantsData = useSelector((state) => state.restaurants);
  const restaurants = restaurantsData.restaurants;
  const sessionUser = useSelector((state) => state.session.user);
  console.log("restaurants", restaurants);

  useEffect(() => {
    dispatch(thunkGetAllRestaurants());
  }, [dispatch]);

  if (!restaurantsData || !restaurantsData.restaurants) return null;

  return (
    <div className="main-container">
      {ownerMode && (
        <div className="owner-div manage-create-a-new-restaurant">
          <h2 className="manage-restaurants-h1-tag">Manage Your Restaurants</h2>
          {restaurants.length === 0 && (
            <button className="owner-btn create-new-restaurant-btn">
              <NavLink to="/restaurants/new" className="create-new-restaurant-owner" style={{ textDecoration: "none", color: "var(--white)" }}>Create a New Restaurant</NavLink>
            </button>
          )}
        </div>
      )}

      <div className={`${ownerMode ? "ownerRestaurant-main-container ownerRestaurant-grid-container" : "restaurants-main-container grid-container"}`}>
        {restaurants.map((restaurant) => (
          <div className={`${ownerMode ? "ownerRestaurant-restaurant-img-main-div" : "restaurant-img-main-div"}`} key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`} style={{ textDecoration: "none", color: "var(--black)" }}>
              <div className={`restaurant-box ${ownerMode ? "ownerRestaurant" : ""}`} title={restaurant.name}>
                <img src={restaurant.image} className={ownerMode ? "ownerRestaurant-img" : "restaurant-img"} alt={restaurant.name} />
                <div className="restaurant-info-flex">
                  <p className="p-card-style location-p-tag">{`${restaurant.location}`}</p>
                  <p className="avgRating-p-tag">★{restaurant.avgRating ? restaurant.avgRating.toFixed(1) : <span className="boldText">New</span>}</p>
                  <p className="p-style"><span className="span-style">${restaurant.price}</span> per person</p>
                </div>
              </div>
            </Link>
            {ownerMode && (
              <div className="owner-div update-delete-btns">
                <button className="owner-btn post-delete-review-btn" onClick={() => history.push(`/restaurants/edit/${restaurant.id}`)}>Update</button>
                {/* Implement DeleteRestaurant component similar to DeleteSpot */}
                {/* <OpenModalButton buttonText="Delete" modalComponent={<DeleteRestaurant restaurantId={restaurant.id} />} /> */}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
