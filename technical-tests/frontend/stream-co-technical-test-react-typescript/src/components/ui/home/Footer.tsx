
import './home.css';
import Facebook from "../../../assets/social/facebook-white.svg"
import Instagram from "../../../assets/social/instagram-white.svg"
import Twitter from ".././../../assets/social/twitter-white.svg"
import AppStore from "../../../assets/stores/play-store.svg"
import MicrosoftStore from "../../../assets/stores/windows-store.svg"
import IOSStore from "../../../assets/stores/app-store.svg"
function Footer() {
    return (
        <footer className='footer-container'>
            <div className='footer-content'>
                <div className='footer-links'>
                    <ul>
                        <li>Home</li>
                        <li>Terms and Conditions</li>
                        <li>Privacy Policy</li>
                        <li>Collection Statement</li>
                        <li>Help</li>
                        <li>Manage Account</li>
                    </ul>
                </div>
                <p className='footer-copyright'>Copyright © 2025 DEMO Streaming. All Rights Reserved.</p>
                <div className='footer-social-media-links'>
                    <div className='icons-container'>
                        <img className='social-media-icon' src={Facebook} alt='Facebook icon' />
                        <img className='social-media-icon' src={Instagram} alt='Instagram icon' />
                        <img className='social-media-icon' src={Twitter} alt="Twitter icon" />
                    </div>

                    <div className='icons-container'>
                        <img className='social-media-store' src={AppStore} alt='App store icon' />
                        <img className='social-media-store' src={IOSStore} alt='IOS store icon' />
                        <img className='social-media-store' src={MicrosoftStore} alt='Microsoft store icon' />
                    </div>
                </div>

            </div>
        </footer>
    );
}

export default Footer;