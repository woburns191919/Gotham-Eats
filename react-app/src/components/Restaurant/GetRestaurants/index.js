import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useHistory, NavLink } from "react-router-dom";
import { thunkGetAllRestaurants } from "../../../store/restaurants";
import {}
import OpenModalButton from "../../OpenModalButton/index";

import "./GetRestaurants.css";


let thunkGetRestaurantsUserOwns=7

export default function GetRestaurants({ ownerMode = false }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const restaurantsData = useSelector((state) => state.restaurants.allRestaurants);
  // const restaurantsData = useSelector((state) => state.restaurants);
  const restaurants = restaurantsData.restaurants;
  console.log('this is restaurants',restaurants)
  const sessionUser = useSelector((state) => state.session.user);
  console.log("restaurants", restaurants);



function findPrev(restaurant){
    for (let prevImg of restaurant.menu_item_images){
      if (prevImg.preview){
        return prevImg.url
      }
    }


}

  useEffect(() => {
    if (ownerMode===false) dispatch(thunkGetAllRestaurants());
    else if(ownerMode===true) dispatch(thunkGetRestaurantsUserOwns())
}, [dispatch,ownerMode]);


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


        {restaurants.map((restaurant,index) => (
          <div className={`${ownerMode ? "ownerRestaurant-restaurant-img-main-div" : "restaurant-img-main-div"}`} key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`} style={{ textDecoration: "none", color: "var(--black)" }}>
              <div className={`restaurant-box ${ownerMode ? "ownerRestaurant" : ""}`}>
              <img key={index}
                  src={
                    `${process.env.PUBLIC_URL}${findPrev(restaurant)}`}
                    className={ownerMode ? "ownerRestaurant-img" : "restaurant-img"} alt="" />




                <div className="restaurant-info-flex">
                  <p className="res-name">{restaurant.name}({restaurant.streetAddress})</p>
                  <p className="avgRating-p-tag">{restaurant.avgRating ? restaurant.avgRating.toFixed(1) : <span className="boldText">New</span>}</p>
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
