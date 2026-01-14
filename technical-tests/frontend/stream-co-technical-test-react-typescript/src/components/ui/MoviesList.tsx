
import Card from "./Card"
import type { Entry } from "../../features/get-series-movies/domain"
import './list.css'
import { useMoviesSeries } from "../../hooks/useMoviesSeries"

export default function MoviesList() {

    const {data, isLoading, error} = useMoviesSeries("movies")
    
    if (isLoading) {
        return <div>Loading...</div>
    }

    if (error) {
        return <div>Oops something went wrong</div>
    }



    return (
        <ul className="list-container">
            {data.map((movie: Entry) => (
                <li key={movie.title}>
                    <Card>
                        <Card.Content backgroundImage={movie.images["Poster Art"].url}>
                            <Card.Title>{movie.title}</Card.Title>
                        </Card.Content>
                    </Card>
                </li>
            ))}
        </ul>
    
    )
}