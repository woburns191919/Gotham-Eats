
import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory,useParams } from "react-router-dom";
import { thunkCreateRestaurant, thunkGetRestaurantDetail,thunkUpdateRestaurant } from "../../../store/restaurants";

import TextInput from "../../Inputs/TextInput";
import { LabeledInput } from "../../Inputs/LabeledInput";
import { LabeledTextarea } from "../../Inputs/LabeledTextarea";
import SelectInput from "../../Inputs/SelectInput";
import "./RestaurantForm.css";

export default function RestaurantForm({ formType, restaurantId }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const sessionUser = useSelector((state) => state.session.user);
  const ourRestaurant= useSelector((state)=>state.restaurants.singleRestaurant)
  const [refreshCount, setRefreshCount] = useState(0);
  const [formData, setFormData] = useState({
    name: "",
    streetAddress: "",
    city: "Gotham",
    state: "New York",
    postalCode: "",
    country: "United States",
    description: "",
    hours: "",
    previmg: "",
  });
  let {id}=useParams()


  console.log(ourRestaurant)

  useEffect(() => {

    if (formType === "Edit" && restaurantId) {
      dispatch(thunkGetRestaurantDetail(restaurantId)).then((data) => {
        setFormData({
          name: data.name,
          streetAddress: data.streetAddress,
          city: data.city,
          state: data.state,
          postalCode: data.postalCode,
          country: data.country,
          description: data.description,
          hours: data.hours,
          previmg: data.previmg,
        });
      });
    }
    if (ourRestaurant === undefined && refreshCount < 1) {
      setRefreshCount((prevCount) => prevCount + 1);
    }
  }, [dispatch, formType, restaurantId,refreshCount]);



  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (formType === "Create") {
        const newlyCreateRestaurant = await dispatch(
          thunkCreateRestaurant(formData)
        );
        if (newlyCreateRestaurant.id) {
          history.push(`/restaurants/${newlyCreateRestaurant.id}`);
        } else {

          throw new Error("Failed to create restaurant");
        }
      }

      if (formType === "Edit") {
        const updatedRestaurant = {
          ...formData,
          id: restaurantId,
        };

        const updatedRestaurantData = await dispatch(
          thunkUpdateRestaurant(updatedRestaurant)
        );

        if (updatedRestaurantData.id) {

          history.push(`/restaurants/${updatedRestaurantData.id}`);
        } else {

          throw new Error("Failed to update restaurant");
        }
      }
    } catch (error) {
      console.error("Error processing the restaurant:", error.message);
    }
  };
    return (
      <div className="restaurant-form-container">
        <h2>{formType === "Edit" ? "Edit Restaurant" : "Create Restaurant"}</h2>
        <form onSubmit={handleSubmit}>

          <TextInput
            label="Name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />

          <LabeledInput
            label="Street Address"
            name="streetAddress"
            value={formData.streetAddress}
            onChange={handleInputChange}
            required
          />

          <LabeledInput
            label="City"
            name="city"
            value={formData.city}
            onChange={handleInputChange}
          />

          <LabeledInput
            label="State"
            name="state"
            value={formData.state}
            onChange={handleInputChange}
          />

          <TextInput
            label="Postal Code"
            name="postalCode"
            value={formData.postalCode}
            onChange={handleInputChange}
            required
          />

          <LabeledInput
            label="Country"
            name="country"
            value={formData.country}
            onChange={handleInputChange}
          />

          <LabeledTextarea
            label="Description"
            name="description"
            value={formData.description}
            onChange={handleInputChange}
            required
          />

          <LabeledTextarea
            label="Hours"
            name="hours"
            value={formData.hours}
            onChange={handleInputChange}
            required
          />

          <TextInput
            label="Preview Image"
            name="previmg"
            value={formData.previmg}
            onChange={handleInputChange}
            required
          />

          <button type="submit">
            {formType === "edit" ? "Update Restaurant" : "Create Restaurant"}
          </button>
        </form>
      </div>
    );
  };




// // // import React, { useState } from "react";
// // // import { useDispatch } from "react-redux";
// // // import { useHistory } from "react-router-dom";

// // // import TextInput from "../../Inputs/TextInput";
// // // import { LabeledInput } from "../../Inputs/LabeledInput";
// // // import { LabeledTextarea } from "../../Inputs/LabeledTextarea";
// // // import { createRestaurantThunk } from "../../../store/restaurants";

// // // import './RestaurantForm.css';

// // // export default function RestaurantForm({ formType, restaurantId }) {
// // //   const dispatch = useDispatch();
// // //   const history = useHistory();


// // //   const [formData, setFormData] = useState({
// // //     name: "",
// // //     streetAddress: "",
// // //     city: "Gotham",
// // //     state: "New York",
// // //     postalCode: "",
// // //     country: "United States",
// // //     description: "",
// // //     hours: "",
// // //     previmg: "",
// // //   });


// // //   const handleInputChange = (e) => {
// // //     const { name, value } = e.target;
// // //     setFormData({
// // //       ...formData,
// // //       [name]: value,
// // //     });
// // //   };


// // //   const handleSubmit = async (e) => {
// // //     e.preventDefault();
// // //     try {
// // //       const createdRestaurant = await dispatch(createRestaurantThunk(formData));
// // //       console.log("Restaurant created:", createdRestaurant);
// // //       history.push("/");
// // //     } catch (error) {

// // //       console.error("Error creating restaurant:", error);
// // //     }
// // //   };


// //   // return (
// //   //   <div className="restaurant-form-container">
// //   //     <h2>{formType === "edit" ? "Edit Restaurant" : "Create Restaurant"}</h2>
// //   //     <form onSubmit={handleSubmit}>

// //   //       <TextInput
// //   //         label="Name"
// //   //         name="name"
// //   //         value={formData.name}
// //   //         onChange={handleInputChange}
// //   //         required
// //   //       />

// //   //       <LabeledInput
// //   //         label="Street Address"
// //   //         name="streetAddress"
// //   //         value={formData.streetAddress}
// //   //         onChange={handleInputChange}
// //   //         required
// //   //       />

// //   //       <LabeledInput
// //   //         label="City"
// //   //         name="city"
// //   //         value={formData.city}
// //   //         onChange={handleInputChange}
// //   //       />

// //   //       <LabeledInput
// //   //         label="State"
// //   //         name="state"
// //   //         value={formData.state}
// //   //         onChange={handleInputChange}
// //   //       />

// //   //       <TextInput
// //   //         label="Postal Code"
// //   //         name="postalCode"
// //   //         value={formData.postalCode}
// //   //         onChange={handleInputChange}
// //   //         required
// //   //       />

// //   //       <LabeledInput
// //   //         label="Country"
// //   //         name="country"
// //   //         value={formData.country}
// //   //         onChange={handleInputChange}
// //   //       />

// //   //       <LabeledTextarea
// //   //         label="Description"
// //   //         name="description"
// //   //         value={formData.description}
// //   //         onChange={handleInputChange}
// //   //         required
// //   //       />

// //   //       <LabeledTextarea
// //   //         label="Hours"
// //   //         name="hours"
// //   //         value={formData.hours}
// //   //         onChange={handleInputChange}
// //   //         required
// //   //       />

// //   //       <TextInput
// //   //         label="Preview Image"
// //   //         name="previmg"
// //   //         value={formData.previmg}
// //   //         onChange={handleInputChange}
// //   //         required
// //   //       />

// //   //       <button type="submit">
// //   //         {formType === "edit" ? "Update Restaurant" : "Create Restaurant"}
// //   //       </button>
// //   //     </form>
// //   //   </div>
// //   // );
// // // }
