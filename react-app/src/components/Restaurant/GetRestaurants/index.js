import React, { useEffect,useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useHistory, NavLink } from "react-router-dom";
import { thunkGetAllRestaurants, thunkGetRestaurantsUserOwns } from "../../../store/restaurants";
import OpenModalButton from "../../OpenModalButton/index";
import "./GetRestaurants.css";

export default function GetRestaurants({ ownerMode = false }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const restaurantsData = useSelector((state) => state.restaurants.allRestaurants);
  const RestaurantsUserOwns = useSelector((state) => state.restaurants.userOwnedRestaurants)
  const [refresh,setRefresh] = useState(3)
  const sessionUser = useSelector((state) => state.session.user);

  const restaurants = ownerMode ? RestaurantsUserOwns.restaurants : restaurantsData.restaurants
  console.log('RESTAURANTS IS******************', restaurants)

  useEffect(() => {

    ownerMode===false?dispatch(thunkGetAllRestaurants()):dispatch(thunkGetRestaurantsUserOwns())


  }, [dispatch,ownerMode,refresh]);
  return (
  <div className="main-container">
    {ownerMode && RestaurantsUserOwns.length && (
    <div className="owner-div manage-create-a-new-restaurant">
          <h2 className="manage-restaurants-h1-tag">Manage Your Restaurants</h2>

            <button className="owner-btn create-new-restaurant-btn">
              <NavLink to="/restaurants/new" className="create-new-restaurant-owner" style={{ textDecoration: "none", color: "var(--white)" }}>Create a New Restaurant</NavLink>
            </button>

        </div>)}



<div className={`${ownerMode ? "ownerRestaurant-main-container ownerRestaurant-grid-container" : "restaurants-main-container grid-container"}`}>
    {restaurants && restaurants.length > 0 && restaurants.map((restaurant) => (
        <div className={`${ownerMode ? "ownerRestaurant-restaurant-img-main-div" : "restaurant-img-main-div"}`} key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`} style={{ textDecoration: "none", color: "var(--black)" }}>
                <div className={`restaurant-box ${ownerMode ? "ownerRestaurant" : ""}`}>
                    <img src={restaurant.menu_item_images.find((img) => img.preview)?.url || '7'} className={ownerMode ? "ownerRestaurant-img" : "restaurant-img"} alt="" />
                    <div className="restaurant-info-flex">
                        <p className="res-name">{restaurant.name}({restaurant.streetAddress})</p>
                        <p className="avgRating-p-tag">{restaurant.avgRating ? restaurant.avgRating.toFixed(1) : <span className="boldText">New</span>}</p>
                    </div>
                </div>
            </Link>
            </div>))}
            {ownerMode && restaurants && restaurants.length>0(
                <div className="owner-div update-delete-btns">
                    <button className="owner-btn post-delete-review-btn" onClick={() => history.push(`/restaurants/edit/${restaurants.restaurant.id}`)}>Update</button>
                    {/* <OpenModalButton buttonText="Delete" modalComponent={<DeleteRestaurant restaurantId={restaurant.id} />} /> */}
                </div>
            )}
        </div>
   </div>) }
