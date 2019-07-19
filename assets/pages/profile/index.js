import DefaultLayout from '../../components/layouts/default';
import { withAuthSync } from '../../common/utils/auth';

const Profile = () => (
  <DefaultLayout>
    <h1>Profile</h1>
    <h2>Howdy, Jake!</h2>
  </DefaultLayout>
)

export default withAuthSync(Profile);
