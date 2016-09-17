//
//  YStock.h
//  SM
//
//  Created by Pavan on 9/16/16.
//  Copyright © 2016 Pavan Shivareddy. All rights reserved.
//

#ifndef YStock_h
#define YStock_h
#import <Foundation/Foundation.h>

@interface YQL : NSObject

- (NSDictionary *)query:(NSString *)statement;


@end


//Class to store the Stock objects
@interface Stock : NSObject
{
    //NSString *_symbol;
    float _percentage;
}

@property (copy) NSString *Symbol;

- (float) printStockValue;// (NSString *) Symbol;

@end


#endif /* YStock_h */
