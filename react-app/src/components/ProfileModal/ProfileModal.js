import React from 'react';
import { useModal } from '../../context/Modal';
import "./ProfileModal.css"

function ProfileModal({ user }) {
  const { closeModal } = useModal();

  return (
      <div className="profile-modal">
          <h2>User Profile</h2>
          <p>Username: {user.username}</p>
          <p>Email: {user.email}</p>
          <button onClick={closeModal}>Close</button>
      </div>
  );
}

export default ProfileModal;
