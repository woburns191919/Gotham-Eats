import React, { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkgetAllUsers } from "../../../store/session";

import OpenModalButton from "../../OpenModalButton";

import DeleteMenuItem from "../../DeleteMenuItem/DeleteMenuItem";

import "./RestaurantDetail.css";
import MenuItemsDetailsModal from "../../MenuItemsDetailDisplayModal";

export default function RestaurantDetail() {
  console.log(' details component mounting???')
  const dispatch = useDispatch();
  // const [reloadPage, setReloadPage] = useState(false);
  const [isDelivery, setIsDelivery] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const sessionUser = useSelector((state) => state.session.user);
  const handleModalOpen = () => {
    setIsModalOpen(true);
  };

  const handleModalClose = () => {
    setIsModalOpen(false);
  };

  const history = useHistory();
  const { id } = useParams();
  const [restaurantsDetailData, setRestaurantsDetailData] = useState([]);
  const [menuDeetz, setMenuDeetz] = useState([]);
  const [restId, setRestId] = useState(id);

  const users = Object.values(
    useSelector((state) =>
      state.session.allUsers ? state.session.allUsers : []
    )
  );

  const fetchRestaurant = async () => {
    const res = await fetch(`/api/restaurants/${restId}`);
    if (res.ok) {
      const data = await res.json();

      return data;
    } else {
      console.error("Failed to fetch");
      return [];
    }
  };

  const fetchMenuItemDeets = async () => {
    const res = await fetch(`/api/restaurants/getMenuItemDeets/${id}`);

    if (res.ok) {
      const data = await res.json();
      setMenuDeetz(data);

      return data;
    } else {
      console.error("Failed to fetch");
      return [];
    }
  };

  useEffect(() => {
    (async function () {
      const restaurantData = await fetchRestaurant();
      setRestaurantsDetailData(restaurantData);
    })();
  }, []);

  useEffect(() => {
    if (restId) {
      fetchMenuItemDeets(menuDeetz);
    }
  }, []);

  useEffect(() => {
    dispatch(thunkgetAllUsers());
  }, [dispatch]);

  let drinks = menuDeetz?.drink || [];
  let entrees = menuDeetz?.entree || [];
  let sides = menuDeetz?.side || [];
  let desserts = menuDeetz?.dessert || [];

  const allMenuItems = [...drinks, ...entrees, ...desserts, ...sides];
  if (
    !restaurantsDetailData ||
    !restaurantsDetailData.menu_item_images ||
    restaurantsDetailData.menu_item_images.length === 0
  ) {
    return null;
  }

  return (
    <>
      <div className="Res-Det-Container">


        {restaurantsDetailData?.owner_id === sessionUser?.id && (
          <h2>we did it </h2>
        )}
        <div className="top-photo">
          <img
            src={`${process.env.PUBLIC_URL}${restaurantsDetailData.menu_item_images[0].url}`}
            alt="Preview"
          />
        </div>
        <div className="res-container">
          <h1 className="det-name">{restaurantsDetailData.name}</h1>
          <div className="det-ratings">
            <h3>
              ★{restaurantsDetailData.avgRating} (
              {restaurantsDetailData.reviews.length} ratings) · $$ · Read
              Reviews · More Info{" "}
            </h3>
          </div>

          { <OpenModalButton buttonText="More Info" modalComponent={<restaurantsDetailData.description
        />} /> }
          <div className="slider-container">
            <div className="label-container">
              <span className={isDelivery ? "active" : ""}>Delivery</span>
              <span className="time">45min</span>
            </div>
            <div className="switch" onClick={() => setIsDelivery(!isDelivery)}>
              <div
                className={isDelivery ? "thumb delivery" : "thumb pickup"}
              ></div>
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
                  <MenuItemsDetailsModal
                    MenuDeetz={drinks}
                    onClose={handleModalClose}
                  />
                }
                onClick={handleModalOpen}
              />
              <OpenModalButton
                buttonText="All Entrees"
                className="mod-bttn"
                modalComponent={
                  <MenuItemsDetailsModal
                    MenuDeetz={entrees}
                    onClose={handleModalClose}
                  />
                }
                onClick={handleModalOpen}
              />
              <OpenModalButton
                buttonText="All Desserts"
                className="mod-bttn"
                modalComponent={
                  <MenuItemsDetailsModal
                    MenuDeetz={desserts}
                    onClose={handleModalClose}
                  />
                }
                onClick={handleModalOpen}
              />
              <OpenModalButton
                buttonText="All Sides"
                className="mod-bttn"
                modalComponent={
                  <MenuItemsDetailsModal
                    MenuDeetz={sides}
                    onClose={handleModalClose}
                  />
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
                  <div className="menu-item-price">
                    ${parseFloat(item.price).toFixed(2)}
                  </div>
                  {restaurantsDetailData?.owner_id === sessionUser?.id && (
                    <div className="delete-menu-item">
                      <button
                        onClick={(e) => {
                          history.push("/");
                        }}
                      >
                        Update
                      </button>
                      <OpenModalButton
                        className="delete-it"
                        buttonText="Delete"
                        modalComponent={<DeleteMenuItem menuItemId={item.id} />}
                      />
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
          <div className="reviews">
            <h4 className="review-name">Reviews</h4>
            <ul className="reviewsList">
              {restaurantsDetailData.reviews?.map((review) => (
                <li key={review.id}>
                  <span className="reviewText">{review.review}</span>
                  <span className="reviewDate">
                    {new Date(review.updated_at).toLocaleDateString()}
                  </span>
                  {users && (
                    <span className="reviewUser">
                      {
                        users.find((user) => user.id === review.user_id)
                          ?.username
                      }
                    </span>
                  )}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </>
  );
}
