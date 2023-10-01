import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';


export const thunkCreateMenuItem = createAsyncThunk(
  'menuItems/create',
  async ({restaurantId, ...menuItemData}, { rejectWithValue }) => {
    try {
      console.log('*******************Sending data:', menuItemData);
      const res = await fetch(`/api/restaurant/${restaurantId}/menu_items`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(menuItemData),
      });


      let resData;
      try {
        resData = await res.json();
      } catch (error) {
        console.error('Error parsing response:', error);
        return rejectWithValue('Error parsing server response');
      }


      if (res.ok) {
        const { message, id } = resData;
        return { message, id, ...menuItemData };
      } else {
        return rejectWithValue(resData);
      }
    } catch (error) {
      console.error('Network or other error:', error);
      return rejectWithValue(error.message);
    }
  }
);


const initialState = {
  allMenuItems: {},
  singleMenuItem: {},
  error: null,
};


const menuItemSlice = createSlice({
  name: 'menuItems',
  initialState,
  reducers: {
    actionSetSingleMenuItem: (state, action) => {
      state.singleMenuItem = action.payload;
    },
    actionSetCreatedMenuItem: (state, action) => {
      state.singleMenuItem = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(thunkCreateMenuItem.fulfilled, (state, action) => {
        state.singleMenuItem = action.payload;
        state.error = null;
      })
      .addCase(thunkCreateMenuItem.rejected, (state, action) => {


        state.error = action.payload;
      });
  },
});


export const {
  actionSetSingleMenuItem,
  actionSetCreatedMenuItem,
} = menuItemSlice.actions;


export default menuItemSlice.reducer;




