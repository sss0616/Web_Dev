import { Routes } from '@angular/router';
import {CompaniesComponent} from "./companies/companies.component";

export const routes: Routes = [
  {
    path: 'companies',
    component: CompaniesComponent,
    title: 'Companies'
  }
];
