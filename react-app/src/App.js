import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch, useParams } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import GetRestaurants from "./components/Restaurant/GetRestaurants";
import RestaurantDetail from "./components/Restaurant/RestaurantDetail";
import MenuItemForm from './components/MenuItems/MenuItemForm';
import Home from "./components/Home";
import CreateRestaurantForm from "./components/Restaurant/RestaurantForm/CreateRestaurantForm";
import EditRestaurantForm from "./components/Restaurant/RestaurantForm/EditRestaurantForm";
import RestaurantForm from "./components/Restaurant/RestaurantForm";

function App() {
  const dispatch = useDispatch();
  const { restaurantId } = useParams();
  const [previewImgUrl, setPreviewImgUrl] = useState("");
  const [menuItemData, setMenuItemData] = useState([]);

  const [isLoaded, setIsLoaded] = useState(false);


  const fetchMenuItemData = async (restaurantId) => {
    try {
      const response = await fetch(`/api/restaurants/${restaurantId}/menu_items`);
      if (response.ok) {
        const data = await response.json();
        setMenuItemData(data);
      }
    } catch (error) {
      console.error("Error fetching menu item data:", error);
    }
  };

  // useEffect(() => {
  //   (async function () {
  //     const menuItemData = await fetchMenuItemData();
  //     setMenuItemData(menuItemData);
  //   })();
  // }, []);

  useEffect(() => {
    // dispatch(fetchMenuItemData(menuItemData))
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);



  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/restaurants/new">
            <CreateRestaurantForm formTye="Create" previewImgUrl={previewImgUrl} />
          </Route>
          <Route path="/restaurants/edit/:restaurantId">
            <RestaurantForm formType="Edit" />
          </Route>
          <Route exact path="/restaurants/:id">
            <RestaurantDetail menuItemData={menuItemData} />
          </Route>
          <Route exact path="/restaurants/:id/menu_items/new">
            <MenuItemForm formType="Create" />
          </Route>
          <Route path="/restaurants/:id/menu_items/:menuItemId/edit">
            <MenuItemForm />
          </Route>
          <Route path="/restaurants">
            <GetRestaurants previewImgUrl={previewImgUrl} />
          </Route>
          <Route path="/login">
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/owner/restaurants/:id">
            <GetRestaurants ownerMode={true} />
          </Route>
          <Route>Page Not Found</Route>
        </Switch>
      )}
    </>
  );
}

export default App;
