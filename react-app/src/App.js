import React, { useState, useEffect } from "react";

import { useDispatch } from "react-redux";
import { Route, Switch, useParams } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
// import LoginFormModal from "./components/LoginFormModal";
// import SignupFormModal from "./components/SignupFormModal";
import GetRestaurants from "./components/Restaurant/GetRestaurants";
import RestaurantDetail from "./components/Restaurant/RestaurantDetail";

import Home from "./components/Home";


import CreateRestaurantForm from "./components/Restaurant/RestaurantForm/CreateRestaurantForm";
import EditRestaurantForm from "./components/Restaurant/RestaurantForm/EditRestaurantForm";

function App() {
  const dispatch = useDispatch();
  const { restaurantId } = useParams();
  const [previewImg, setPreviewImg] = useState("");


  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
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
          <Route path="/restaurants/new">
            <CreateRestaurantForm setPreviewImg={setPreviewImg}/>
          </Route>
          <Route path="/restaurants/edit/:id">
            <EditRestaurantForm />
          </Route>
          <Route exact path="/restaurants/:id">
            <RestaurantDetail />
          </Route>

          <Route path="/restaurants">
            <GetRestaurants previewImg={previewImg}/>
            {/* <Route path="/restaurants" >
            <GetRestaurants />
            </Route> */}
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
