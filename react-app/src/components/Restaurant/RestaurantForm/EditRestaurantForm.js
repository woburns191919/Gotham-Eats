import { useParams } from "react-router-dom";
import { useState } from "react";
import RestaurantForm from './index';

export default function EditRestaurantForm() {

  const { restaurantId } = useParams();
  // console.log('restId?***', restaurantId)
  // const [refreshCount,setRefreshCount]=useState(0)
  return (
    <>
    <RestaurantForm
      formType="Edit"
      restaurantId={restaurantId}
    />
    </>
    );
}
