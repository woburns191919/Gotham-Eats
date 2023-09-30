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

  const handleModalOpen = () => {
    setIsModalOpen(true);
  };


  const handleModalClose = () => {
    setIsModalOpen(false);
  };

  const users = Object.values(
    useSelector((state) => (state.session.allUsers ? state.session.allUsers : []))
  );

  const menuDeets= useSelector((state)=>(state.restaurants?.RestaurantMenu))


  const restaurantsDetailData = useSelector((state) => state.restaurants?.singleRestaurant);

  console.log('use selector users', users)

  let drinks= menuDeets?.drinks
  let entrees= menuDeets?.entrees
  let sides= menuDeets?.sides
  let desserts= menuDeets?.desserts


  console.log("********************restaurantsDetailData", restaurantsDetailData)
  if (restaurantsDetailData && restaurantsDetailData.menu_item_images && restaurantsDetailData.menu_item_images.length > 0) {

  }

  function findPrev(restaurant) {
    for (let prevImg of restaurant.menu_item_images) {
      if (prevImg.preview) {
        return prevImg.url
      }
    }
  }

  if (!menuDeets){
    setRefreshCount(refreshCount+1)
  }

  useEffect(() => {

    dispatch(thunkGetRestaurantDetail(id));
  }, [dispatch,id,refreshCount]);

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
          <div>
          <OpenModalButton
            buttonText="All drinks"
            modalComponent={
              <MenuItemsDetailsModal MenuDeetz={drinks} onClose={handleModalClose} />
            }
            onClick={handleModalOpen}
          />
          <OpenModalButton
            buttonText="All Entrees"
            modalComponent={
              <MenuItemsDetailsModal MenuDeetz={entrees} onClose={handleModalClose} />
            }
            onClick={handleModalOpen}
          />
          <OpenModalButton
            buttonText="All Desserts"
            modalComponent={
              <MenuItemsDetailsModal MenuDeetz={desserts} onClose={handleModalClose} />
            }
            onClick={handleModalOpen}
          />
          <OpenModalButton
            buttonText="All Sides"
            modalComponent={
              <MenuItemsDetailsModal MenuDeetz={sides} onClose={handleModalClose}  />
            }
            onClick={handleModalOpen}
          />


          </div>

          <div className="imgages-container">
            {restaurantsDetailData.menu_item_images.slice(0).map((img, index) => (
              <img className="res-det-photo"
                key={index}
                src={`${process.env.PUBLIC_URL}${img.url}`}
                alt=""
              />

              // {restaurantsDetailData.menu_item_images.url}
            ))}
          </div>

        </div>
        <div className="reviews">
          <h2>Reviews</h2>
            <ul className='reviewsList'>
              {console.log('data type of restaurant detail',restaurantsDetailData)}
            {restaurantsDetailData.reviews?.map((review)=>
            <li>

              {review.review}
              {review.updated_at}
              {users && users.find(user => user.id === review.user_id)}
              {console.log('users********', users)}
            </li>


            )}




            </ul>
        </div>
      </div>
    </div>)
}
