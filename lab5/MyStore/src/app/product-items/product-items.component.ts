import { Component, EventEmitter, Input, Output } from '@angular/core';
import { products } from '../products'
import { Product } from '../products'

@Component({
  selector: 'app-product-items',
  templateUrl: './product-items.component.html',
  styleUrl: './product-items.component.css'
})
export class ProductItemsComponent {
  @Input () product: Product | undefined;
  @Input () a: any;
  @Output () remove = new EventEmitter();
  isLike = false;

  share(link:string) {
    const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(link)}`;
    window.open(telegramUrl, '_blank');
  }

  deleteProduct(){
    this.remove.emit(this.product?.id);
  }
  like(){
    this.isLike = !this.isLike;
    if(this.isLike && this.product){
      this.product.likes++;
    }
    else if(this.product){
      this.product.likes--;
    }
  }
}
