import DefaultHeader from '../includes/headers/default';

const DefaultLayout = props => (
  <div>
    <DefaultHeader></DefaultHeader>
    {props.children}
  </div>
)

export default DefaultLayout;
