import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// ************************************************
//                   ****Thunks****
// ************************************************

// ***************************thunkGetAllRestaurants**************************

export const thunkGetAllRestaurants = createAsyncThunk(
  'restaurants/getAll',
  async (_, { rejectWithValue }) => {
    try {
      const res = await fetch('/api/restaurants');
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
      const res = await fetch('/api/restaurants', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(restaurantData),
      });

      if (res.ok) {
        const createdRestaurant = await res.json();
        return createdRestaurant;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors);
      }
    } catch (error) {
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
  async (_, { rejectWithValue }) => {
    try {
      const res = await fetch('/api/restaurants/manage');
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
