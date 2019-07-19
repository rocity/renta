import Head from 'next/head';
import DefaultHeader from '../includes/headers/default';


const DefaultLayout = props => (
  <div>
    <Head>
      <title>Renta Project</title>
    </Head>
    <DefaultHeader></DefaultHeader>
    {props.children}
  </div>
)

export default DefaultLayout;
