import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useHistory, NavLink, useParams } from "react-router-dom";
import restaurants, { thunkGetAllRestaurants, thunkGetRestaurantsUserOwns } from "../../../store/restaurants";
import { thunkGetAllRestaurantReviews } from "../../../store/reviews";
import OpenModalButton from "../../OpenModalButton/index";
import "./GetRestaurants.css";


export default function WillexGetRestaurants({ ownerMode = false }) {

  const history = useHistory();
  const [restaurants, setRestaurants] = useState();

  const sessionUser = useSelector((state) => state.session.user);
  console.log('logged in user', sessionUser)

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

  useEffect(() => {
    (async function () {
       const restaurantData = await fetchRestaurants();
       setRestaurants(restaurantData);
     }())
   }, []);








  const dispatch = useDispatch();


  const restaurantsData = useSelector((state) => state.restaurants?.allRestaurants);
  const RestaurantsUserOwns = useSelector((state) => state.restaurants?.RestaurantsUserOwns)
  // const reviews = useSelector((state) => state.reviews && state.reviews.allReviews)


  const [refreshCount, setRefreshCount] = useState(0);




//   const restaurants = ownerMode ? RestaurantsUserOwns : restaurantsData?.restaurants
//   const fetchData2= async(id) =>{
//     let goal= await dispatch(thunkGetRestaurantsUserOwns(sessionUser.id));
//     return goal
// }

// useEffect(() => {
//   if (!sessionUser?.id) return;
//   if (!restaurants) {
//       if (!RestaurantsUserOwns) dispatch(thunkGetRestaurantsUserOwns(sessionUser.id));
//   } else {
//     if (!restaurantsData?.restaurants) dispatch(thunkGetAllRestaurants());

//   }
// }, [ sessionUser?.id, ownerMode, RestaurantsUserOwns, restaurantsData?.restaurants]);






  return (

    <div className="main-container">
      <h1>WE ARE IN WILLEX</h1>
      {ownerMode && RestaurantsUserOwns.length && (
        <div className="owner-div manage-create-a-new-restaurant">
          <h2 className="manage-restaurants-h1-tag">Manage Your Restaurants</h2>

          <button className="owner-btn create-new-restaurant-btn">
            <NavLink to="/restaurants/new" className="create-new-restaurant-owner" style={{ textDecoration: "none", color: "var(--white)" }}>Create a New Restaurant</NavLink>
          </button>

        </div>)}



      <div className={`${ownerMode ? "ownerRestaurant-main-container ownerRestaurant-grid-container" : "restaurants-main-container grid-container"}`}>
        {restaurants && restaurants?.length > 0 && restaurants.map((restaurant) => (
          <div className={`${ownerMode ? "ownerRestaurant-restaurant-img-main-div" : "restaurant-img-main-div"}`} key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`} style={{ textDecoration: "none", color: "var(--black)" }}>
              <div className={`restaurant-box ${ownerMode ? "ownerRestaurant" : ""}`}>
                <img src={restaurant.menu_item_images.find((img) => img.preview)?.url || '7'} className={ownerMode ? "ownerRestaurant-img" : "restaurant-img"} alt="" />
                <div className="restaurant-info-flex">
                  <p className="res-name">{restaurant.name}({restaurant.streetAddress})</p>
                  <p className="avgRating-p-tag">
                    {/* {restaurant.avgRating && restaurant.avgRating ? restaurant.avgRating?.toFixed(1) : <span className="boldText">New</span>} */}
                    {(restaurant.avgRating !== null && restaurant.avgRating !== undefined) ? restaurant.avgRating : <span className="boldText">New</span>}</p>
                </div>

              </div>
            </Link>
          </div>
          ))}

        {ownerMode && restaurants && restaurants.length > 0 && restaurants.map((restaurant, i) => (
          <div key={i} className="owner-div update-delete-btns">
            <button className="owner-btn post-delete-review-btn" onClick={() => history.push(`/restaurants/edit/${restaurant.id}`)}>Update</button>
            <button className="owner-btn post-delete-review-btn" onClick={() => history.push(`/restaurants/edit/${restaurant.id}`)}>Delete</button>
            {console.log('owner mode', ownerMode)}
            {/*LETS GET TH IS UP AND RUNNING BOYS <OpenModalButton buttonText="Delete" modalComponent={<DeleteRestaurant restaurantId={restaurant.id} />} /> */}
          </div>
        ))}
      </div>
    </div>)
}
