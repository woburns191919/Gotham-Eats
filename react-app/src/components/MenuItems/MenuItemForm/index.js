import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import useFormValidation from "../../Inputs/handlesHelperFunctions"


import { useHistory } from 'react-router-dom';
import { thunkCreateMenuItem, actionSetCreatedMenuItem } from '../../../store/menuItem';


export default function MenuItemForm({ formType, menuItemId }) {
    const dispatch = useDispatch();
    const history = useHistory();
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [price, setPrice] = useState('');
    const [type, setType] = useState('');


    const { validationObj, handleInputChange } = useFormValidation();
    const [initialRestaurant, setInitialRestaurant] = useState({});


    const menuItem = useSelector((state) => state.menuItem.singleMenuItem);
    const sessionUser = useSelector((stateid) => stateid.session.user);
    console.log('*************menuItem', menuItem);


    const handleCreateMenuItem = async (menuItemData) => {
        const resultAction = await dispatch(thunkCreateMenuItem(menuItemData));
        if (thunkCreateMenuItem.fulfilled.match(resultAction)) {
            const newlyCreatedMenuItem = resultAction.payload;
            dispatch(actionSetCreatedMenuItem(newlyCreatedMenuItem));
            history.push(`/menuItems/${newlyCreatedMenuItem.id}`);
        }
    };


    const handleSubmit = (e) => {
        e.preventDefault();
        const menuItemData = { restaurantId: sessionUser.restaurant_id, name, description, price, type };
        if (formType === "Create") handleCreateMenuItem(menuItemData);


    };


    return (
        <form onSubmit={handleSubmit}>
            <label>
                Name:
                <input
                    type="text"
                    value={name}
                    onChange={handleInputChange(setName, 'name')}
                />
            </label>
            <label>
                Description:
                <textarea
                    value={description}
                    onChange={handleInputChange(setDescription, 'description')}
                />
            </label>
            <label>
                Price:
                <input
                    type="number"
                    value={price}
                    onChange={handleInputChange(setPrice, 'price')}
                />
            </label>
            <label>
                Type:
                <select
                    value={type}
                    onChange={handleInputChange(setType, 'type')}
                >
                    <option value="" disabled selected>Select a Menu Item Type</option>
                    <option value="entree">Entree</option>
                    <option value="dessert">Dessert</option>
                    <option value="drink">Drink</option>
                    <option value="side">Side</option>
                </select>
            </label>
            <button type="submit">Create Menu Item</button>
        </form>
    );
};
