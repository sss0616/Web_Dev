import {Component, OnInit} from '@angular/core';
import {Company, Vacancy} from "../models";
import {CompanyService} from "../Services/company.service";
import {VacancyService} from "../Services/vacancy.service";
import {RouterLink} from "@angular/router";
import {NgForOf, NgIf} from "@angular/common";


@Component({
  selector: 'app-companies',
  standalone: true,
  imports: [RouterLink, NgForOf, NgIf],
  templateUrl: './companies.component.html',
  styleUrl: './companies.component.css'
})
export class CompaniesComponent implements OnInit{
  companies!: Company[];
  vacancies: Vacancy[] = [];
  company_vacancies: Vacancy[] = [];
  showCompany_vacancies: boolean = false;
  constructor(private companyService: CompanyService, private vacancyService: VacancyService){
    this.companies = [];
  }

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe((companies) =>{
      this.companies = companies;
    });
    this.vacancyService.getVacancies().subscribe((data: Vacancy[])=> {
      this.vacancies = data;
    });
  }




  getCompanyVacancies(company: Company){
    this.showCompany_vacancies = !this.showCompany_vacancies;
    this.vacancyService.getCompanyVacancies(company.id).subscribe((data: Vacancy[])=> {
      this.company_vacancies = data;
    })
  }
}
