import React from 'react';
// import { useModal } from '../../context/Modal';
import "./menuItemsDetail.css"


function MenuItemsDetailsModal({ MenuDeetz }) {
  // const { closeModal } = useModal();

  return (
    <div className="profile-modal">
      <div className="imgages-container">
        {MenuDeetz.map((ele, index) => (
          <div key={index} className="menu-item-wrapper">
            <img className="res-det-photo-mod"
              src={`${ele.url}`}
              alt={`${ele.name}`}
            />
            <div className="menu-item-name">{ele.name}</div>
            <div className="menu-item-price">${parseFloat(ele.price).toFixed(2)}</div>
          </div>
        ))}
      </div>
    </div>
  );
}


export default MenuItemsDetailsModal;
