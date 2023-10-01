import { useParams } from "react-router-dom";
import { useState } from "react";
import MenuItemForm from './index';


export default function EditMenuItemForm() {


    const { menuItemId } = useParams();
    return (
        <>
            <MenuItemForm
                formType="Edit"
                menuItemId={menuItemId}
            />
        </>
    );
}
