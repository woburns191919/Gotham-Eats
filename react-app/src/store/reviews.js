import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// ***************************thunkGetAllRestaurantReviews**************************
export const thunkGetAllRestaurantReviews = createAsyncThunk(
  'reviews/getAllRestaurantReviews',
  async (restaurantId, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/${restaurantId}/reviews`);
      if (res.ok) {
        const data = await res.json();
        return data.reviews;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors.message); 
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ***************************thunkCreateRestaurantReview**************************
export const thunkCreateRestaurantReview = createAsyncThunk(
  'reviews/createRestaurantReview',
  async ({ restaurantId, review, stars }, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/${restaurantId}/reviews`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ review, stars }),
      });

      if (res.ok) {
        const data = await res.json();
        return data.review;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors.message);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ***************************thunkUpdateRestaurantReview**************************
export const thunkUpdateRestaurantReview = createAsyncThunk(
  'reviews/updateRestaurantReview',
  async ({ restaurantId, reviewId, review }, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/${restaurantId}/reviews/${reviewId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ review }),
      });

      if (res.ok) {
        const data = await res.json();
        return data.review;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors.message);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ***************************thunkDeleteRestaurantReview**************************
export const thunkDeleteRestaurantReview = createAsyncThunk(
  'reviews/deleteRestaurantReview',
  async ({ restaurantId, reviewId }, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/restaurants/${restaurantId}/reviews/${reviewId}`, {
        method: 'DELETE',
      });

      if (res.ok) {
        return reviewId;
      } else {
        const errors = await res.json();
        return rejectWithValue(errors.message);
      }
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// ************************************************
//                   ****Reducer****
// ************************************************

const initialState = {
  allReviews: [],
  singleReview: null,
  isLoading: false,
  error: null,
};

const reviewSlice = createSlice({
  name: 'reviews',
  initialState,
  reducers: {
    actionSetAllReviews: (state, action) => {
      state.allReviews = action.payload;
    },
    actionSetSingleReview: (state, action) => {
      state.singleReview = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(thunkGetAllRestaurantReviews.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(thunkGetAllRestaurantReviews.fulfilled, (state, action) => {
        state.isLoading = false;
        state.allReviews = action.payload;
      })
      .addCase(thunkGetAllRestaurantReviews.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      })
      .addCase(thunkCreateRestaurantReview.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(thunkCreateRestaurantReview.fulfilled, (state, action) => {
        state.isLoading = false;
        state.singleReview = action.payload;
      })
      .addCase(thunkCreateRestaurantReview.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      })
      .addCase(thunkUpdateRestaurantReview.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(thunkUpdateRestaurantReview.fulfilled, (state, action) => {
        state.isLoading = false;
        state.singleReview = action.payload;
      })
      .addCase(thunkUpdateRestaurantReview.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      })
      .addCase(thunkDeleteRestaurantReview.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(thunkDeleteRestaurantReview.fulfilled, (state, action) => {

        const deletedReviewId = action.payload;
        state.allReviews = state.allReviews.filter((review) => review.id !== deletedReviewId);
      })
      .addCase(thunkDeleteRestaurantReview.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      });
  },
});

export const { actionSetAllReviews, actionSetSingleReview } = reviewSlice.actions;
export default reviewSlice.reducer;
