import Link from 'next/link';

const DefaultHeader = () => (
  <header>
    <h2>Header</h2>
    <ul>
      <li>
        <Link href="/"><a>Home</a></Link>
      </li>
      <li>
        <Link href="/listings"><a>Listings</a></Link>
      </li>
    </ul>

    <style jsx>
      {`
      li {
        display: inline;
        margin-right: 10px;
      }
      `}
    </style>
  </header>
)
export default DefaultHeader;
