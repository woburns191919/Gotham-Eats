import React from 'react';
import { useModal } from '../../context/Modal';


async function MenuItemsDetailsModal({ MenuDeetz }) {
    const { closeModal } = useModal();

    return (
        <div className="profile-modal">
         <div className="imgages-container">
            {MenuDeetz.map((ele, index) => (
              <img className="res-det-photo"
                key={index}
                src={`${ele.url}`}
                alt={`${ele.name}`}
              />

              // {restaurantsDetailData.menu_item_images.url}
            ))}
          </div>
        </div>
    );
  }

  export default MenuItemsDetailsModal;
