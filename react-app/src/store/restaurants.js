// import { fetch } from "./csrf";




// ************************************************
//                   ****types****
// ************************************************
const GET_ALL_RESTAURANTS = "/get_all_restaurants";
const GET_SINGLE_RESTAURANT = "/get_single_restaurant";
const CREATE_RESTAURANT = "create_restaurant";
const UPDATE_RESTAURANT = "update_restaurant";
const DELETE_RESTAURANT = "delete_restaurant";
const GET_ALL_RESTAURANTS_OF_CURRENT_USER = "/get_all_restaurants_of_user";


// ************************************************
//                   ****action creator****
// ************************************************
const actionGetRestaurants = (restaurants) => ({ type: GET_ALL_RESTAURANTS, restaurants });
const actionGetSingleRestaurant = (restaurant) => ({ type: GET_SINGLE_RESTAURANT, restaurant });
const actionCreateRestaurant = (restaurant) => ({ type: CREATE_RESTAURANT, restaurant });
const actionUpdateRestaurant = (restaurant) => ({ type: UPDATE_RESTAURANT, restaurant });
const actionDeleteRestaurant = (id) => ({ type: DELETE_RESTAURANT, id });
const actionGetAllOwnerRestaurants = (restaurants) => ({ type: GET_ALL_RESTAURANTS_OF_CURRENT_USER, restaurants });


// ************************************************
//                   ****Thunks****
// ************************************************

// ***************************thunkGetAllRestaurants**************************

export const thunkGetAllRestaurants = () => async (dispatch) => {
  try {
    const res = await fetch("/api/restaurants");
    if (res.ok) {
      const data = await res.json();
      console.log("Data from /api/restaurants:", data); // Log the response data
      // dispatch(actionGetRestaurants(normalizeArr(data)));
      dispatch(actionGetRestaurants(data));
      return data;
    } else {
      const errors = await res.json();
      return errors;
    }
  } catch (error) {
    console.error("Error fetching restaurants:", error);
    return error;
  }
};

// ***************************thunkGetOwnerAllRestaurants**************************
export const thunkGetOwnerAllRestaurants = () => async (dispatch) => {
  const res = await fetch("/api/restaurants/current");
  if (res.ok) {
    const Restaurants = await res.json();
    dispatch(actionGetAllOwnerRestaurants(Restaurants));
    return Restaurants;
  } else {
    const errors = await res.json();
    return errors;
  }
};

// // ***************************thunkGetRestaurantDetail**************************
// export const thunkGetRestaurantDetail = (restaurantId) => async (dispatch) => {
//   const res = await fetch(`/api/restaurants/${restaurantId}`);
//   if (res.ok) {
//     const Restaurant = await res.json();
//     dispatch(actionGetSingleRestaurant(Restaurant));
//     return Restaurant;
//   } else {
//     const errors = await res.json();
//     return errors;
//   }
// };

// // ***************************thunkGetRestaurantDetail**************************

// export const thunkCreateRestaurant = (newRestaurant, restaurantImages, sessionUser) => async (dispatch) => {

//   const res = await fetch("/api/restaurants", {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify(newRestaurant),
//   });

//   if (res.ok) {
//     const newlyCreatedRestaurant = await res.json();

//     const newImagesRes = await Promise.all(restaurantImages.map(async (imageObj) => {
//       const imageRes = await fetch(`/api/restaurants/${newlyCreatedRestaurant.id}/images`, {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(imageObj),
//       });
//       if(imageRes.ok) {
//         const imageData = await imageRes.json();
//         return imageData;
//       }
//     }));

//     newlyCreatedRestaurant.RestaurantImages = newImagesRes;
//     newlyCreatedRestaurant.ownerName = sessionUser.username;

//     dispatch(actionCreateRestaurant(newlyCreatedRestaurant));
//     return newlyCreatedRestaurant;
//   } else {
//     const errors = await res.json();
//     return errors;
//   }
// };

// export const thunkUpdateRestaurant = (updatedRestaurant) => async (dispatch) => {
//   const res = await fetch(`/api/restaurants/${updatedRestaurant.id}`, {
//     method: "PUT",
//     headers: {
//       "Content-Type": "application/json"
//     },
//     body: JSON.stringify(updatedRestaurant)
//   });

//   if (res.ok) {
//     const data = await res.json();
//     const editedRestaurant = data;
//     dispatch(thunkGetRestaurantDetail(editedRestaurant.id));
//     return editedRestaurant;
//   } else {
//     const errors = await res.json();
//     return errors;
//   }
// };

// export const thunkDeleteRestaurant = (restaurantId) => async (dispatch) => {
//   const res = await fetch(`/api/restaurants/${restaurantId}`, {
//     method: 'DELETE',
//   });

//   if (res.ok) {
//     dispatch(actionDeleteRestaurant(restaurantId));
//   } else {
//     const errors = await res.json();
//     return errors;
//   }
// };




// ************************************************
//                   ****Reducer****
// ************************************************
function normalizeArr(restaurants) {
  const normalizedRestaurants = {};
  restaurants.forEach((restaurant) => (normalizedRestaurants[restaurant.id] = restaurant));
  return normalizedRestaurants;
}

const initialState = { allRestaurants: [], singleRestaurant: {} };

// ************************************************
export default function restaurantReducer(state = initialState, action) {
  let newState;
  switch (action.type) {
    case GET_ALL_RESTAURANTS:
      return { ...state, allRestaurants: action.restaurants };
    // case GET_SINGLE_RESTAURANT:
    //   newState = { ...state, singleRestaurant: {} };
    //   newState.singleRestaurant = action.restaurant;
    //   return newState;
    // case CREATE_RESTAURANT:
    //   newState = { ...state };
    //   newState.singleRestaurant = action.restaurant;
    //   return newState;
    // case UPDATE_RESTAURANT:
    //   newState = { ...state, singleRestaurant: {} };
    //   newState.singleRestaurant = action.restaurant;
    //   return newState;
    // case DELETE_RESTAURANT:
    //   newState = { allRestaurants: {...state.allRestaurants}, singleRestaurant: {} };
    //   delete newState.allRestaurants[action.id];
    //   return newState;
    // case GET_ALL_RESTAURANTS_OF_CURRENT_USER:
    //   newState = { ...state, allRestaurants: {} };
    //   newState.allRestaurants = action.restaurants;
    //   return newState;
    default:
      return state;
  }
}
