import React, {useState,useSelector} from "react"


import { useDispatch } from "react-redux";
import { useModal } from "../../../context/Modal";


import { thunkDeleteRestaurant, thunkGetOwnerAllRestaurants } from "../../../store/restaurants";


import "DeleteRestaurant.css";


export function DeleteRestaurant({restaurantId}) {
  const restaurantsData = useSelector((state) => state)
  const {closeModal}= useModal()
  const dispatch = useDispatch()







  return null
}
