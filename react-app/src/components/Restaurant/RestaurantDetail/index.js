import React, { useEffect, useState } from "react";
import { useParams, useHistory, NavLink, Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkgetAllUsers } from "../../../store/session";
import CreateMenuItemForm from "../../MenuItemsDetailDisplayModal";
import OpenModalButton from "../../OpenModalButton";
import DeleteMenuItem from "../../DeleteMenuItem/DeleteMenuItem";
import "./RestaurantDetail.css";
import MenuItemsDetailsModal from "../../MenuItemsDetailDisplayModal";

export default function RestaurantDetail() {
  // console.log("details component mount?");
  const dispatch = useDispatch();
  const [isDelivery, setIsDelivery] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [reloadPage, setReloadPage] = useState(false);
  const [itmImgUrl, setItmImgUrl] = useState(null);
  const [awsArray, setAwsArray] = useState(null);


  const sessionUser = useSelector((state) => state.session.user);
  const handleModalOpen = () => {
    setIsModalOpen(true);
  };

  const handleModalClose = () => {
    setIsModalOpen(false);
  };

  const history = useHistory();
  const [restaurantsDetailData, setRestaurantsDetailData] = useState(null);
  const [menuDeetz, setMenuDeetz] = useState([]);
  const { id } = useParams();
  const [restId, setRestId] = useState(id);

  const users = Object.values(
    useSelector((state) =>
      state.session.allUsers ? state.session.allUsers : []
    )
  );

  const fetchRestaurant = async () => {
    const res = await fetch(`/api/restaurants/${restId}`);
    console.log("restaurant id from details", restId);
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

  const handleDelete = async (itemId) => {
    try {
      const response = await fetch(`/api/restaurants/${id}/menu_items/${itemId}`, {
        method: "DELETE",
      });

      if (response.ok) {

        window.location.reload();
      } else {
        console.error("Failed to delete menu item. Status:", response.status);
        const errorData = await response.json();
        console.error("Error data:", errorData);
      }
    } catch (error) {
      console.error("Failed to delete menu item: ", error);
    }
  };



  useEffect(() => {
    (async function () {
      const restaurantData = await fetchRestaurant();
      setRestaurantsDetailData(restaurantData);
    })();
  }, [restId]);

  useEffect(() => {
    if (restId) {
      fetchMenuItemDeets(menuDeetz);
    }
  }, [restId]);

  useEffect(() => {
    dispatch(thunkgetAllUsers());
  }, [dispatch]);

  useEffect(() => {
    const userImages = restaurantsDetailData?.menu_items?.filter(
      (item) => item.itm_img_url
    );
    setItmImgUrl(userImages);
  }, [restaurantsDetailData]);



  // console.log('huge array', restaurantsDetailData?.menu_items)

  let drinks = menuDeetz?.drink || [];
  let entrees = menuDeetz?.entree || [];
  let sides = menuDeetz?.side || [];
  let desserts = menuDeetz?.dessert || [];

  const allMenuItems = [...drinks, ...entrees, ...desserts, ...sides];

  if (!restaurantsDetailData) {
    return null;
  }




  return (
    <div className="Res-Det-Container">
       <div className="top-photo">
          <img
            src={`${process.env.PUBLIC_URL}${restaurantsDetailData?.menu_item_images[0]?.url}`}
            alt="Preview"
          />
        </div>
      <div className="res-container">
        <h1 className="det-name">{restaurantsDetailData?.name}</h1>
        <div className="det-ratings">
          <h3>
            ★{restaurantsDetailData.avgRating} (
            {restaurantsDetailData?.reviews?.length} ratings) · $$ · Read
            Reviews · More Info{" "}
          </h3>
        </div>

        <OpenModalButton
          buttonText="More Info"
          modalComponent={restaurantsDetailData.description}
        />

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
                {item.restaurant_id === restId && item.itm_img_url === null ? (
                  <img
                    className="res-det-photo"
                    src={item.url}
                    alt={item.name}
                  />
                ) : (
                  <img className="res-det-photo" src={item.url} />
                )}

                <div className="menu-item-name">{item.name}</div>
                <div className="menu-item-price">
                  ${parseFloat(item.price).toFixed(2)}
                </div>
                {restaurantsDetailData?.owner_id === sessionUser?.id && (
                  <div className="delete-menu-item">
                    <button className="delete-it"
                      onClick={() => handleDelete(item.id)}
                    >
                      Delete
                    </button>
                  <div className="delete-menu-item">
                    <Link
                    to={`/restaurants/${id}/menu_items/${item.id}/edit`}
                    style={{ textDecoration: "none", color: "var(--black)" }}
                    >
                    <button className="delete-it">
                      Update
                    </button>
                      </Link>
                  </div>
                  </div>
                )}
              </div>
            ))}
          </div>
          <div className="imgages-container">
            {restaurantsDetailData.menu_items?.map((item, index) => (
                item.restaurant_id == restId && item.itm_img_url &&
              <div className="menu-item-wrapper" key={index}>
                  <img
                    className="res-det-photo"
                    src={item.itm_img_url}
                    alt={item.name}
                  />


                <div className="menu-item-name">{item.name}</div>
                <div className="menu-item-price">
                  ${parseFloat(item.price).toFixed(2)}
                </div>
                {restaurantsDetailData?.owner_id === sessionUser?.id && (
                  <div className="delete-menu-item">
                  <button className="delete-it"
                    onClick={() => handleDelete(item.id)}
                  >
                    Delete
                  </button>
                  <div className="delete-menu-item">
                    <Link
                    to={`/restaurants/${id}/menu_items/${item.id}/edit`}
                    style={{ textDecoration: "none", color: "var(--black)" }}
                    >
                    <button className="delete-it">
                      Update
                    </button>
                      </Link>
                  </div>
                </div>
                )}
              </div>
            ))}
          </div>

          {sessionUser && <div className="create-new-restaurant-owner">
            <NavLink
              className="reviews"
              to={`/restaurants/${restId}/menu_items/new`}
              style={{ textDecoration: "none", color: "var(--white)" }}
            >
              Add a Menu Item
            </NavLink>
          </div>
                    }
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
                    {users.find((user) => user.id === review.user_id)?.username}
                  </span>
                )}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}
