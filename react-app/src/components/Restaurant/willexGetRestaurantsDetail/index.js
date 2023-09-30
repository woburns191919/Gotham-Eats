import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetMenuItemsDeets, thunkGetRestaurantDetail } from "../../../store/restaurants";
import OpenModalButton from "../../OpenModalButton";
import { thunkgetAllUsers } from "../../../store/session";

import "./WillexGetRestaurantDetail.css";
import MenuItemsDetailsModal from "../../MenuItemsDetailDisplayModal";

export default function WillexGetRestaurantDetail() {
  const dispatch = useDispatch();
  const [reloadPage, setReloadPage] = useState(false);
  const { id } = useParams();
  const [isDelivery, setIsDelivery] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [refreshCount, setRefreshCount] = useState(0);
  const MAX_RETRIES = 3;

  const handleModalOpen = () => {
    setIsModalOpen(true);
  };


  const handleModalClose = () => {
    setIsModalOpen(false);
  };

  const users = Object.values(
    useSelector((state) => (state.session.allUsers ? state.session.allUsers : []))
  );

  const menuDeetz = useSelector((state) => (state.restaurants?.RestaurantMenu))


  const restaurantsDetailData = useSelector((state) => state.restaurants?.singleRestaurant);

  console.log("Menudeetz ********", menuDeetz)

  let drinks = menuDeetz?.drink || [];
  let entrees = menuDeetz?.entree || [];
  let sides = menuDeetz?.side || [];
  let desserts = menuDeetz?.dessert || [];

  const allMenuItems = [...drinks, ...entrees, ...desserts, ...sides];



  if (restaurantsDetailData && restaurantsDetailData.menu_item_images && restaurantsDetailData.menu_item_images.length > 0) {

  }

  function findPrev(restaurant) {
    for (let prevImg of restaurant.menu_item_images) {
      if (prevImg.preview) {
        return prevImg.url
      }
    }
  }

  if (!menuDeetz && refreshCount < MAX_RETRIES) {
    setRefreshCount(prev => prev + 1);
  }

  useEffect(() => {

    dispatch(thunkGetRestaurantDetail(id));
  }, [dispatch, id, refreshCount]);

  useEffect(() => {
    dispatch(thunkgetAllUsers())
  }, [dispatch])

  useEffect(() => {
    dispatch(thunkGetMenuItemsDeets(id))
  }, [dispatch])


  if (
    !restaurantsDetailData ||
    !restaurantsDetailData.menu_item_images ||
    restaurantsDetailData.menu_item_images.length === 0
  ) {
    return null;
  }

  console.log("DRinks ********", drinks)
  return (
    <div className="Res-Det-Container">
      <h1>WE ARE IN WILLEX</h1>
      <div className="top-photo">
        <img
          src={`${process.env.PUBLIC_URL}${restaurantsDetailData.menu_item_images[0].url}`} alt="Preview" />
      </div>
      <div className="res-container">
        <h1 className="det-name">{restaurantsDetailData.name}</h1>
        <div className="det-ratings"><h3>★{restaurantsDetailData.avgRating}{" "}({restaurantsDetailData.reviews.length} ratings) · $$ · Read Reviews · More Info  </h3>

        </div>

        {/* <OpenModalButton buttonText="More Info" modalComponent={<restaurantsDetailData.description
        />} /> */}
        <div className="slider-container">
          <div className="label-container">
            <span className={isDelivery ? "active" : ""}>Delivery</span>
            <span className="time">45min</span>
          </div>
          <div className="switch" onClick={() => setIsDelivery(!isDelivery)}>
            <div className={isDelivery ? "thumb delivery" : "thumb pickup"}></div>
          </div>
          <div className="label-container">
            <span className={!isDelivery ? "active" : ""}>Pickup</span>
            <span className="time">15min</span>
          </div>
        </div>
        <div className="menu-items">
          <h2 className="nat-sel">Natural Selection</h2>
          <div className="mod-bbtn">
            <OpenModalButton
              buttonText="All drinks"
              className="mod-bttn"
              modalComponent={
                <MenuItemsDetailsModal MenuDeetz={drinks} onClose={handleModalClose} />
              }
              onClick={handleModalOpen}
            />
            <OpenModalButton
              buttonText="All Entrees"
              className="mod-bttn"
              modalComponent={
                <MenuItemsDetailsModal MenuDeetz={entrees} onClose={handleModalClose} />
              }
              onClick={handleModalOpen}
            />
            <OpenModalButton
              buttonText="All Desserts"
              className="mod-bttn"
              modalComponent={
                <MenuItemsDetailsModal MenuDeetz={desserts} onClose={handleModalClose} />
              }
              onClick={handleModalOpen}
            />
            <OpenModalButton
              buttonText="All Sides"
              className="mod-bttn"
              modalComponent={
                <MenuItemsDetailsModal MenuDeetz={sides} onClose={handleModalClose} />
              }
              onClick={handleModalOpen}
            />


          </div>

          <div className="imgages-container">
            {allMenuItems.map((item, index) => (
              <div className="menu-item-wrapper" key={index}>
                <img
                  className="res-det-photo"
                  src={item.url}
                  alt={item.name}
                />
                <div className="menu-item-name">{item.name}</div>
                <div className="menu-item-price">${parseFloat(item.price).toFixed(2)}</div>
              </div>
            ))}
          </div>


        </div>
        <div className="reviews">
          <h4 className="review-name">Reviews</h4>
          <ul className='reviewsList'>
            {restaurantsDetailData.reviews?.map((review) =>
              <li key={review.id}>
                <span className="reviewText">{review.review}</span>
                <span className="reviewDate">{new Date(review.updated_at).toLocaleDateString()}</span>
                {users && <span className="reviewUser">{users.find(user => user.id === review.user_id)?.username}</span>}
              </li>
            )}
          </ul>
        </div>
      </div>
    </div >)
}
