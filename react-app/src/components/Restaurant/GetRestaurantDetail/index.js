import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetRestaurantDetail } from "../../../store/restaurants";
import OpenModalButton from "../../OpenModalButton";

import "./GetRestaurantDetail.css";

export default function GetRestaurantDetail() {
  const dispatch = useDispatch();
  const { id } = useParams();



  const restaurantsDetailData = useSelector((state) => state.restaurants.singleRestaurant);
  if (restaurantsDetailData && restaurantsDetailData.menu_item_images && restaurantsDetailData.menu_item_images.length > 0) {
    // console.log("Num Reviews ********", restaurantsDetailData.)
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
        <h1>{restaurantsDetailData.name}</h1>
        <div className="det-ratings">★{restaurantsDetailData.avgRating.toFixed(1)}({restaurantsDetailData.reviews.length} ratings)</div>
      </div>
    </div>
  )
}
