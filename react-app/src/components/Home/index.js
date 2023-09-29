import React from "react";
import { useHistory } from "react-router-dom";
import './home.css'

export default function Home() {
    const history = useHistory();

    function handleDirectionChange(event) {
        const selectedDirection = event.target.value;
      


        if (['west', 'east', 'north', 'south'].includes(selectedDirection)) {
            history.push('/restaurants');
        }
    }

    return (
        <>
            <select onChange={handleDirectionChange} className="batman-dropdown">
                <option value="" disabled selected>Gotham Precinct</option>
                <option value="west">West</option>
                <option value="east">East</option>
                <option value="north">North</option>
                <option value="south">South</option>
            </select>
        </>
    )
}
