// import { useDispatch } from "react-redux";
// import { useModal } from "../../context/Modal";
// // import { thunkDeleteMenuItem } from "../../store/menuItem"
// import { thunkGetRestaurantsUserOwns } from "../../store/restaurants";

// export default function DeleteMenuItem({ menuItemId }) {
//     const dispatch = useDispatch();
//     const { closeModal } = useModal();


//     const deleteMenuItemCallBack = async () => {
//         await dispatch(thunkDeleteMenuItem(menuItemId));
//         await dispatch(thunkGetRestaurantsUserOwns());
//         closeModal();
//     }

//     return (
//         <>
//             <div className="delete-container">
//                 <h1 className="confirm-delete">Confirm Delete</h1>
//                 <p className="delete-writing">Are you sure you want to delete this menu item? This action cannot be undone.</p>
//                 <button className="delete-da-bttn" onClick={deleteMenuItemCallBack}>Yes (Delete Menu Item) </button>
//                 <button className="cancel-delete" onClick={closeModal}>No (Keep Menu Item)</button>
//             </div>
//         </>
//     );

// }
