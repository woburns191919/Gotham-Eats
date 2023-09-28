import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import LoginFormModal from "./components/LoginFormModal";
import SignupFormModal from "./components/SignupFormModal";
import GetRestaurants from "./components/Restaurant/GetRestaurants";
import Home from "./components/Home"
import GetRestaurantDetail from "./components/Restaurant/GetRestaurantDetail";
import CreateRestaurantForm from "./components/Restaurant/RestaurantForm/CreateRestaurantForm";
import EditRestaurantForm from "./components/Restaurant/RestaurantForm/EditRestaurantForm";

function App() {
  const dispatch = useDispatch();


  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);


  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/" >
            <Home />
          </Route>
          <Route path="/restaurants/new" >
            <CreateRestaurantForm />
          </Route>
          <Route path="/restaurants/edit/:id" >
            <EditRestaurantForm />
          </Route>
          <Route path="/restaurants/:id" >
            <GetRestaurantDetail />
          </Route>
          <Route path="/restaurants" >
            <GetRestaurants />
          </Route>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/owner/restaurants/:ownerId">
            <GetRestaurants ownerMode={true} />
          </Route>
          <Route>Page Not Found</Route>
        </Switch>
      )}
    </>
  );
}

export default App;
