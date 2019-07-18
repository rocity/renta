import Link from 'next/link';
import DefaultLayout from '../../components/layouts/default';

const ListingLink = props => (
  <li>
    <Link href="/listings/p/[id]" as={`/listings/p/${props.id}`}>
      <a>{props.id}</a>
    </Link>
  </li>
)

const Index = () => (
  <DefaultLayout>
    <h1>Listings</h1>
    <ul>
      <ListingLink id="listing-one" />
      <ListingLink id="listing-two" />
      <ListingLink id="listing-three" />
    </ul>
  </DefaultLayout>
);

export default Index;
