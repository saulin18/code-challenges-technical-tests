
import { NavLink } from 'react-router'
import placeholderImage from '../../../assets/placeholder.png'
import Card from '../Card'


function Main() {
  return (
    <section className='main-container'>
      <NavLink to="/series">
        <Card>
          <Card.Content backgroundImage={placeholderImage}>
            <Card.Title>Series</Card.Title>
          </Card.Content>
        </Card>
        <Card.Description>Popular series</Card.Description>
      </NavLink>
      <NavLink to="/movies">
        <Card>
          <Card.Content backgroundImage={placeholderImage}>
            <Card.Title>Movies</Card.Title>
          </Card.Content>
        </Card>
        <Card.Description>Popular movies</Card.Description>
      </NavLink>

    </section>
  )
}

export default Main