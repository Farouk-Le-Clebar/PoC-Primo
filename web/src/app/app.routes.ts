import { Routes } from '@angular/router';
import { MapComponent } from './map/map.component';
import { LoginComponent } from './login/login.component';
import { DisplayParcelleInfoComponent } from './map/display-parcelle-info/display-parcelle-info.component';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  { path: 'map', component: MapComponent },
  { path: 'login', component: LoginComponent },
  { path: 'display', component: DisplayParcelleInfoComponent },
  { path: '', component: HomeComponent },
];
