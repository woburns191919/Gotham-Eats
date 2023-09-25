import React, { useState, useEffect, useRef } from "react";
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import OpenModalMenuItem from './OpenModalMenuItem';
import './Navigation.css';

function Navigation({ isLoaded }) {
    const sessionUser = useSelector(state => state.session.user);
    const [showMenu, setShowMenu] = useState(false);
    const ulRef = useRef();
    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = (e) => {
            if (!ulRef.current.contains(e.target)) {
                setShowMenu(false);
            }
        };

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener("click", closeMenu);
    }, [showMenu]);

    const closeMenu = () => setShowMenu(false);

    return (
        <>
            <div className="navBar-container">
                <div className="navBar-inner-container">

                    <div className="navBar-left">
                        {sessionUser && (
                            <div className="navBar-create-link">
                                {/* <NavLink to="/resaurants/new" className="create-new-spot">
                                    Add your restaurant
                                </NavLink> */}
                            </div>
                        )}
                        {isLoaded && (
                            <ul>
                                <li>
                                    <ProfileButton user={sessionUser} showMenu={showMenu} />
                                </li>
                            </ul>

                        )}
                        <NavLink exact to="/" className="navbar-logo">
                            <h1>Gotham Eats</h1>
                        </NavLink>
                    </div>


                    <div className="navBar-spacer"></div>


                    <div className="navBar-right">
                        <NavLink to="/cart" className="cart-btn">
                            <i className="fas fa-shopping-cart" style={{ marginRight: '6px' }}></i>Cart
                        </NavLink>
                        {sessionUser ? null : (
                            <>

                                <OpenModalMenuItem
                                    className="login-btn"
                                    itemText={
                                        <span>
                                            <i className="fas fa-user"></i> Log in
                                        </span>
                                    }
                                    onItemClick={closeMenu}
                                    modalComponent={<LoginFormModal />}
                                />
                                <OpenModalMenuItem
                                    className="signup-btn"
                                    itemText="Sign up"
                                    onItemClick={closeMenu}
                                    modalComponent={<SignupFormModal />}
                                />
                                {/* <NavLink to="/login" className="login-btn">
                                    <i className="fas fa-user"></i> Log in

                                </NavLink>
                                <NavLink to="/signup" className="signup-btn">Sign up</NavLink> */}
                            </>
                        )}
                    </div>
                </div>
            </div>
        </>
    );
}


export default Navigation;


// // 	return (
// // 		<ul>
// // 			<li>
// // 				<NavLink exact to="/">Home</NavLink>
// // 			</li>
// // 			{isLoaded && (
// // 				<li>
// // 					<ProfileButton user={sessionUser} />
// // 				</li>
// // 			)}
// // 		</ul>
// // 	);
// // }

// // export default Navigation;
