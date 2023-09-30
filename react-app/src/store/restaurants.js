import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
//constants
const GET_MENU_ITEMS_DETAILS = "restaurants/get_details_bro";

//oldschool actions
const Get_Deets_Separate_Type_1restaurant = (MenuItemsAndImages) => ({
	type: GET_MENU_ITEMS_DETAILS,
	payload: MenuItemsAndImages,
});

// ************************************************
//                   ****Thunks****
// ************************************************

// ***************************thunkGetAllRestaurants**************************

export const thunkGetAllRestaurants = createAsyncThunk(
  'restaurants/getAll',
  async (_, { rejectWithValue }) => {
    try {
      const res = await fetch('/api/restaurants/getMenuItemDeets');
      if (res.ok) {
        const data = await res.json();

        return data;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);
//**************************thunkGetMenuItemsDeets********** */
export const thunkGetMenuItemsDeets = createAsyncThunk(
  'restaurants/MenuItemDeets',
  async (rest_id, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/getMenuItemDeets/${rest_id}`);
      if (res.ok) {
        const allMenuItems = await res.json();
        return allMenuItems;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ***************************thunkGetRestaurantDetail**************************

export const thunkGetRestaurantDetail = createAsyncThunk(
  'restaurants/getDetail',
  async (restaurantId, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/${restaurantId}`);

      if (res.ok) {
        const restaurant = await res.json();
        return restaurant;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ***************************thunkCreateRestaurant**************************

export const thunkCreateRestaurant = createAsyncThunk(
  'restaurants/create',
  async (restaurantData, { rejectWithValue }) => {
    try {
      const res = await fetch('/api/restaurants/new', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(restaurantData),
      });

      if (res.ok) {
        const createdRestaurant = await res.json();

        // return createdRestaurant;
      } else {
        try {
          const errors = await res.json();
          return rejectWithValue(errors);
        } catch (e) {
          console.error('Error response not JSON:', e);
          const text = await res.text();
          console.error('Error response as text:', text);
          return rejectWithValue(e.message);
        }
      }
    } catch (error) {
      console.error('Network or other error:', error);
      return rejectWithValue(error.message);
    }
  }
);




// ***************************thunkUpdateRestaurant**************************

export const thunkUpdateRestaurant = createAsyncThunk(
  'restaurants/update',
  async (updatedRestaurantData, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/${updatedRestaurantData.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedRestaurantData),
      });

      if (res.ok) {
        const updatedRestaurant = await res.json();
        return updatedRestaurant;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ***************************thunkDeleteRestaurant**************************

export const thunkDeleteRestaurant = createAsyncThunk(
  'restaurants/delete',
  async (restaurantId, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/${restaurantId}`, {
        method: 'DELETE',
      });

      if (res.ok) {
        return restaurantId;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ***************************thunkGetRestaurantsUserOwns**************************

export const thunkGetRestaurantsUserOwns = createAsyncThunk(
  'restaurants/getUserOwnedRestaurants',
  async (ownerId, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/manage/${ownerId}`);
      if (res.ok) {

        const data = await res.json();
        return data;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ************************************************
//                   ****Reducer****
// ************************************************

const initialState = { allRestaurants: {}, singleRestaurant: {}, userOwnedRestaurants: [] };

const restaurantSlice = createSlice({
  name: 'restaurants',
  initialState,
  reducers: {
    actionSetAllRestaurants: (state, action) => {
      state.allRestaurants = action.payload;
    },
    actionSetSingleRestaurant: (state, action) => {
      state.singleRestaurant = action.payload;
    },
    actionSetUserOwnedRestaurants: (state, action) => {
      state.userOwnedRestaurants = action.payload;
    },
    actionSetCreatedRestaurant: (state, action) => {
      state.singleRestaurant = action.payload;
    },
    actionSetUpdatedRestaurant: (state, action) => {
      state.singleRestaurant = action.payload;
    },
    actionSetDeletedRestaurant: (state, action) => {
      const deletedRestaurantId = action.payload;
      const deletedRestaurantIndex = state.userOwnedRestaurants.findIndex(
        restaurant => restaurant.id === deletedRestaurantId
      );

      if (deletedRestaurantIndex !== -1) {
        state.userOwnedRestaurants.splice(deletedRestaurantIndex, 1);
      }
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(thunkGetAllRestaurants.fulfilled, (state, action) => {
        state.allRestaurants = action.payload;
      })
      .addCase(thunkGetRestaurantDetail.fulfilled, (state, action) => {
        state.singleRestaurant = action.payload;
      })
      .addCase(thunkCreateRestaurant.fulfilled, (state, action) => {
        state.singleRestaurant = action.payload;
      })
      .addCase(thunkUpdateRestaurant.fulfilled, (state, action) => {
        state.singleRestaurant = action.payload;
      })
      // .addCase(thunkDeleteRestaurant.fulfilled, (state, action) => {
      //   delete state.allRestaurants[action.payload];
      // })
      .addCase(thunkDeleteRestaurant.fulfilled, (state, action) => {
        const deletedRestaurantId = action.payload;
        const deletedRestaurantIndex = state.userOwnedRestaurants.findIndex(
          restaurant => restaurant.id === deletedRestaurantId
        );

        if (deletedRestaurantIndex !== -1) {
          state.userOwnedRestaurants.splice(deletedRestaurantIndex, 1);
        }
      })
      .addCase(thunkGetRestaurantsUserOwns.fulfilled, (state, action) => {
        state.userOwnedRestaurants = action.payload;
      });
  },
});

export const {
  actionSetAllRestaurants,
  actionSetSingleRestaurant,
  actionSetUserOwnedRestaurants,
  actionSetCreatedRestaurant,
  actionSetUpdatedRestaurant,
  actionSetDeletedRestaurant,
} = restaurantSlice.actions;

export default restaurantSlice.reducer;
