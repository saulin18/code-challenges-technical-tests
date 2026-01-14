
import Button from '../Button'
import './home.css'

function Navbar() {
    return (
        <header>
            <nav className="nav-container">
                <h1 className='nav-title'>DEMO Streaming</h1>
                <div className="nav-buttons-container">
                    <div>
                        <Button label="Login" onClick={() => { }} variant="transparent">
                            Login
                        </Button>
                        <Button label="Start your free trial" onClick={() => { }} variant="secondary">
                            Start your free trial
                        </Button>
                    </div>
                </div>
            </nav>
        </header>
    )
}

export default Navbar