import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useHistory, NavLink } from "react-router-dom";
import { thunkGetAllRestaurants, thunkGetOwnerAllRestaurants } from "../../../store/restaurants";
import OpenModalButton from '../../OpenModalButton/index';

import "./GetRestaurants.css";

export default function GetRestaurants({ ownerMode = false }) {
  return null
}
