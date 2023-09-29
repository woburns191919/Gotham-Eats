import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetRestaurantDetail } from "../../../store/restaurants";
import OpenModalButton from "../../OpenModalButton";

import "./GetRestaurantDetail.css";

export default function GetRestaurantDetail() {
  const dispatch = useDispatch();
  const [reloadPage, setReloadPage] = useState(false);
  const { id } = useParams();
  const [isDelivery, setIsDelivery] = useState(true);



  const restaurantsDetailData = useSelector((state) => state.restaurants?.singleRestaurant);
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

  useEffect(() => {
    dispatch(thunkGetRestaurantDetail(id));
  }, [dispatch]);

  if (
    !restaurantsDetailData ||
    !restaurantsDetailData.menu_item_images ||
    restaurantsDetailData.menu_item_images.length === 0
  ) {
    return null;
  }


  return (
    <div className="Res-Det-Container">
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

        </div>
      </div>
    </div>
  )
}
